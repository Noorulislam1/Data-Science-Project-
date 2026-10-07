# Stage One: Project Introduction and Data Understanding

## Project title

**Exploratory Data Analysis of Electric Vehicle Charging Patterns**

## Project background

Electric vehicles are becoming more common, increasing the need for reliable and efficiently managed charging infrastructure. Understanding how people use public charging stations can help cities and organizations plan station locations, evaluate demand, reduce unnecessary charger occupancy, and improve the charging experience.

This project analyzes electric vehicle charging sessions recorded by the City of Palo Alto, California. The first stage focuses on understanding the dataset and defining the questions that will guide the full analysis.

## Project objectives

The main objectives are to:

- Identify when charging stations experience the highest demand.
- Study how charging activity changes over time.
- Examine the relationship between charging duration and energy delivered.
- Compare usage among charging stations.
- Compare weekday and weekend behavior.
- Investigate seasonal charging patterns.
- Measure how long vehicles remain connected after charging finishes.

## Dataset overview

| Item | Description |
| --- | --- |
| Dataset | Electric Vehicle Charging Station Usage |
| Provider | City of Palo Alto |
| Time period | July 2011–December 2020 |
| Original records | 259,415 charging sessions |
| Columns | 33 |
| Unique stations | 47 |
| Main file | `EVChargingStationUsage.csv` |

The dataset contains information such as session start and end times, charging duration, total connection duration, energy delivered, station information, port or plug details, and charging fees.

## Research questions

1. At what hours and on which days are charging stations used most?
2. How has the number of charging sessions changed over the years?
3. Is charging duration related to the amount of energy delivered?
4. Which stations have the highest number of sessions?
5. Is charging behavior different on weekdays and weekends?
6. Are there meaningful seasonal patterns?
7. How much idle time occurs after active charging is complete?

## Initial data-quality checks

The first inspection includes:

- Reviewing the dataset shape, columns, and data types.
- Examining sample records.
- Counting missing values.
- Detecting exact duplicate records.
- Checking whether timestamps can be parsed correctly.
- Looking for negative energy values or invalid durations.
- Checking whether active charging time exceeds total connection time.

These checks help distinguish unusable records from unusual but potentially valid charging sessions.

## Initial observations

- The dataset covers several years and is suitable for time-series analysis.
- Date and time fields can support hourly, daily, monthly, yearly, and seasonal comparisons.
- Charging duration and total connection duration represent different behaviors.
- Idle time can be calculated by subtracting active charging time from total connection time.
- Station names make it possible to compare demand and behavior across locations.
- Extreme values should be investigated before deciding whether to remove them.

## Planned analysis workflow

```text
Collect data
    ↓
Inspect structure and quality
    ↓
Clean invalid and duplicate records
    ↓
Create time and usage features
    ↓
Calculate descriptive statistics
    ↓
Create visualizations
    ↓
Interpret findings and document limitations
```

## Expected deliverables

- A cleaned analytical dataset
- A reproducible Jupyter notebook
- Hourly, daily, monthly, seasonal, and station-level summaries
- Data visualizations
- A written report explaining the findings and limitations

## Files to review next

- [`../EV_Charging_Analysis.ipynb`](../EV_Charging_Analysis.ipynb) — complete analysis notebook
- [`../EVChargingStationUsage.csv`](../EVChargingStationUsage.csv) — original dataset
- [`../PROJECT_RESULTS.md`](../PROJECT_RESULTS.md) — final results summary

