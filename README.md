# UNICEF Immunization Data Processing and Visualization (Python)

## Overview

This project processes and analyzes global immunization data maintained by UNICEF. 

Using object-oriented programming in Python, I built a reusable data-processing class to clean, subset, and visualize vaccine coverage data across regions and years.

The project demonstrates structured data cleaning, transformation, filtering, and visualization using real-world public health data.

---

## Objectives

- Clean and standardize raw immunization data
- Create flexible subsetting methods for region, vaccine, and year
- Map vaccine codes to descriptive labels
- Generate bar and line visualizations for comparative analysis
- Implement reusable functionality using a custom Python class

---

## Dataset

The dataset contains immunization coverage percentages by:

- Region
- Vaccine type
- Year
- Percentage coverage

The raw dataset is read and cleaned within the class initialization process.

No personally identifiable information is included.

---

## Methods

### Data Cleaning

The cleaning pipeline includes:

- Assigning appropriate column names
- Standardizing region names (removing whitespace, replacing symbols)
- Converting year values to consistent string format
- Mapping vaccine codes (e.g., `DTP1`, `BCG`) to full vaccine descriptions

All preprocessing occurs automatically upon instantiation of the `ImmunizationData` class.

---

### Object-Oriented Design

The project is built around a custom class:

`ImmunizationData`

Key methods include:

- `make_subset()`  
  Filters the dataset by region, vaccine type, and/or year.

- `make_plot()`  
  Generates bar or line visualizations from a Pandas Series object.

- `__str__()`  
  Returns a summary of dataset dimensions.

This structure allows for reusable and modular data processing.

---

## Example Analyses

Two example analyses included:

- BCG vaccine coverage by region (2019)
- DTP1 vaccination trends in the East Asia and Pacific region over time

Visualizations are generated using Seaborn and Matplotlib.

---

## Technologies Used

- Python
- Pandas
- Seaborn
- Matplotlib

---
