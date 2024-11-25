import os
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")


def clean_name(name):
    # Convert "{name}, Lake" to "Lake {name}"
    if ", Lake" in name:
        name = f"Lake {name.replace(', Lake', '')}"
    # Replace '/' with a single name (arbitrarily choose first name for now)
    if "/" in name:
        if name == 'Adder Pond/Hopkins Pond':
            name = 'Adder Pond'
        elif name == 'Wash Pond/Sunset Lake':
            name = 'Sunset Lake'
    if name == 'Captains Pond':
        name = 'Captain Pond'
    # Remove extra spaces
    return name.strip()


def geocode(name):
    location = geolocator.geocode(name + ", New Hampshire")
    if location:
        return location.latitude, location.longitude
    return None, None


def main():
    bloom_df = pd.read_csv('Cyanobacteria2024.csv')
    bloom_df['Cleaned_Name'] = bloom_df['LAKE'].apply(clean_name)

    bloom_df["Coordinates"] = bloom_df["LAKE"].apply(geocode)
    bloom_df["Latitude"] = bloom_df["Coordinates"].apply(lambda x: x[0])
    bloom_df["Longitude"] = bloom_df["Coordinates"].apply(lambda x: x[1])

    bloom_df['geometry'] = gpd.points_from_xy(bloom_df['Longitude'], bloom_df['Latitude'])

    gdf = gpd.GeoDataFrame(bloom_df, geometry='geometry')
    gdf.to_file('cyanobacteria_geocoded.gpkg', driver='GPKG', crs='EPSG:4326')


if __name__ == '__main__':
    main()