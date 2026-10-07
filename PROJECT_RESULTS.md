# Project Results: Exploratory Data Analysis of Electric Vehicle Charging Patterns

## 1. Dataset overview

- Source file: `EVChargingStationUsage.csv`
- Original shape: **259,415 rows × 33 columns**
- Original date coverage: **July 29, 2011 to December 31, 2020**
- Unique stations: **47**
- Public dataset reference: City of Palo Alto, Electric Vehicle Charging Station Usage (July 2011–December 2020).

## 2. Cleaning performed

- Removed exact duplicates and sessions with objectively invalid timestamps, negative energy, non-positive durations, or active charging time materially longer than total connection time.
- Retained missing descriptive fields when the session remained analytically usable.
- Retained statistically extreme but internally valid sessions for outlier analysis.
- Original records: **259,415**
- Records removed: **120**
- Final records: **259,295**

## 3. Important descriptive statistics

- Total energy: **2,215,029.06 kWh**
- Average energy/session: **8.54 kWh**
- Median energy/session: **6.87 kWh**
- Average charging duration: **2.00 hours**
- Median charging duration: **1.82 hours**
- Average energy per charging hour: **4.26 kW equivalent**

## 4. Answers to the research questions

1. **When are chargers used most?** The busiest start hour was **11:00**, the busiest day was **Wednesday**, and the busiest calendar month was **January**. Weekdays accounted for **76.1%** of sessions.
2. **How has usage changed over time?** The busiest observed year was **2017** with **48,950 sessions**. The busiest individual month was **2017-05** with **4,982 sessions**. Partial years: **2011 (6 months)**.
3. **Duration and energy:** Pearson correlation was **r = 0.871** (p = 0). Long sessions varied widely in energy, so duration is informative but not sufficient by itself.
4. **Station differences:** The busiest station was **PALO ALTO CA / HAMILTON #2** with **23,706 sessions**. Station summaries show differences in session count, energy, duration, and idle time.
5. **Weekday vs weekend:** Weekend sessions used **-7.6%** average energy and had **-14.5%** average charging time relative to weekdays.
6. **Seasonality:** **Winter** had the most sessions, while **Winter** had the highest average energy per session. Totals are affected by multi-year growth and unequal coverage.
7. **Occupancy and idle behavior:** Average idle time was **0.49 hours**, median idle time was **0.01 hours**, and **12.1%** of sessions had at least one hour of idle time (an analytical threshold, not an official standard).

## 5. Important relationships discovered

- Charging duration and energy had a positive linear association (**r = 0.871**), but extreme duration did not guarantee extreme energy.
- Connection duration reflects both active charging and idle occupancy; these measures should not be used interchangeably.
- The correlation heatmap excludes numeric identifiers because their magnitude has no continuous analytical meaning.

## 6. Interesting or unexpected findings

- Sessions most often began at 11:00; Wednesday was the busiest day of week and January the busiest calendar month.
- The data record 2,215,029 kWh in total, averaging 8.54 kWh per session (median 6.87 kWh).
- Average active charging time was 2.00 hours; median charging time was 1.82 hours.
- Charging duration and energy delivered had a Pearson correlation of 0.871.
- Weekdays represented 76.1% of all sessions.
- Average idle time was 0.49 hours (median 0.01); 12.1% of sessions had at least one hour of idle time.
- The busiest observed year was 2017 with 48,950 sessions; partial years must be interpreted cautiously.
- The busiest individual month was 2017-05 with 4,982 sessions.
- The most-used station was PALO ALTO CA / HAMILTON #2, with 23,706 sessions.

## 7. Limitations

- One geographic area and charging-network context.
- Observational data cannot establish causation.
- Station inventory and policies may have changed over time.
- Partial calendar years: 2011 (6 months).
- Missing descriptive fields and possible logging anomalies.
- Outliers may be legitimate or erroneous; valid extremes were retained.
- No direct measures of queues, unmet demand, trip purpose, or battery state of charge.

## 8. Final conclusion

Palo Alto charging behavior varies materially by time, station, and day type. Energy and active charging duration move together, while connection time also contains meaningful post-charging idle occupancy. The results support evaluating session volume, energy, charging duration, and idle time together, without inferring causes from correlations alone.

## 9. Generated figures

- `figures/charging_sessions_by_hour.png`
- `figures/charging_sessions_by_time.png`
- `figures/correlation_heatmap.png`
- `figures/duration_vs_energy.png`
- `figures/idle_time_distribution.png`
- `figures/monthly_charging_trend.png`
- `figures/optional_clustering_diagnostics.png`
- `figures/outlier_boxplots.png`
- `figures/seasonal_charging_patterns.png`
- `figures/stations_highest_idle_time.png`
- `figures/top_charging_stations.png`
- `figures/weekday_weekend_comparison.png`
