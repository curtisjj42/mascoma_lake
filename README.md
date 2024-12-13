# Cyanobacteria Blooms in New Hampshire Lakes

## Overview

This research project investigates the frequency, severity, and environmental factors contributing to cyanobacteria blooms in lakes across New Hampshire. The primary goal is to understand the trends and factors influencing the occurrence of harmful algal blooms (HABs) and to analyze how land cover, wetland proximity, and other environmental variables affect bloom dynamics.

## Project Objectives

- **Analyze bloom frequency and severity**: Explore temporal and spatial trends in cyanobacteria blooms from 2003–2023.
- **Environmental factors**: Assess the role of wetlands, land use/land cover, and other variables in influencing bloom occurrence.
- **Resilience and mitigation**: Investigate how wetland areas may mitigate the impact of blooms on lake health.
  
## Key Research Questions

1. How do trends in land use and land cover affect the frequency and severity of cyanobacteria blooms?
2. What role do wetlands play in mitigating or exacerbating bloom occurrence in New Hampshire's lakes?
3. How have cyanobacteria bloom events changed over the past 20 years in terms of both frequency?

## Datasets

This project uses a variety of datasets to address these questions:

- **Cyanobacteria Bloom Data (2003-2024)**: A comprehensive dataset detailing bloom occurrences in monitored bodies of water across New Hampshire.
- **Land Cover and Land Use Data**: Historical (1962, 1974, 1998) and contemporary (2015, 2021) datasets for Strafford and Rockingham counties, including impervious surface data.
- **Wetland Spatial Data**: Wetland data for New Hampshire to assess the role of wetland areas near lakes in bloom mitigation.

## Methodology

The following approaches are used for data analysis:

1. **Geospatial Analysis**: 
   - Buffer analysis around lakes to assess the proximity of wetlands and land cover types.
   - Spatial join operations to correlate bloom occurrences with land use and wetland distribution.

2. **Time Series Analysis**:
   - Trend analysis of cyanobacteria bloom occurrences and their relationship to changing land use and cover.

3. **Statistical Modeling**:
   - Predictive models to assess the impact of environmental variables (e.g., wetlands, impervious surfaces, land use) on bloom occurrence.

## Tools and Libraries

The project makes use of the following Python libraries and tools:
- **pandas**: Data manipulation and analysis.
- **geopandas**: Geospatial data handling and analysis.
- **matplotlib**, **seaborn**: Data visualization.
- **scikit-learn**: Machine learning for predictive modeling.
- **shapely**: Geometric operations on spatial data.
- **statsmodels**: Statistical analysis.

## Data Sources

- [Cyanobacteria Bloom Data](https://www.des.nh.gov/contact)
- [Land Use/Land Cover Data](https://new-hampshire-geodata-portal-1-nhgranit.hub.arcgis.com/search?q=land%20cover)
- [Wetland Spatial Data](https://new-hampshire-geodata-portal-1-nhgranit.hub.arcgis.com/search?q=land%20cover)

## Results

For analysis and results, please see the included report
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was made possible by the availability of public datasets from [NH DES].

## Contact

For questions or inquiries, please contact Jason Curtis at [curtisjj42@gmail.com].
