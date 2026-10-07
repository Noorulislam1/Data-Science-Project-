# EV Charging Analysis — Project Proposal

## Problem statement

Public charging stations are shared resources. Demand varies by time and location, while vehicles may remain connected after active charging ends. This project will use historical session data to describe these patterns and identify practical opportunities for better charging-infrastructure planning.

## Scope

The project will analyze recorded charging sessions in Palo Alto from July 2011 through December 2020. It will focus on usage frequency, energy consumption, charging duration, connection duration, idle time, station differences, and time-based patterns.

The project will not attempt to prove why a pattern occurred or predict individual driver behavior. The results will describe associations found in the available observational data.

## Proposed tools

- Python
- Jupyter Notebook
- pandas and NumPy for data preparation
- Matplotlib and Seaborn for visualization
- SciPy for statistical analysis
- scikit-learn for optional clustering

## Success criteria

The project will be considered successful if it:

1. Produces a documented and reproducible cleaning process.
2. Answers the seven research questions with appropriate evidence.
3. Presents clear visualizations and summary tables.
4. Separates active charging time from total connection and idle time.
5. Communicates data limitations without making unsupported causal claims.

## Team discussion points

- Are the research questions clear and useful?
- Should any additional variables be included?
- Which charts will communicate the results most effectively?
- How should extreme sessions be treated?
- Who will be responsible for cleaning, analysis, visualization, and presentation?
