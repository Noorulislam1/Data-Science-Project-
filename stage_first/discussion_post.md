# Project Proposal Discussion Post

**Subject: Group [Your Group Number] – Charge Insights**

## Working Title

**Exploratory Data Analysis of Electric Vehicle Charging Patterns in Palo Alto**

Our project will analyze electric vehicle charging-station usage in Palo Alto, California. We want to understand when charging stations are busiest, how charging demand has changed over time, which stations receive the most use, and how charging time relates to energy consumption. We will also examine idle time—the period when a vehicle remains connected after active charging has ended.

## Dataset Description

We are using the City of Palo Alto Electric Vehicle Charging Station Usage dataset. It contains approximately 259,415 charging sessions recorded from July 2011 through December 2020 across 47 charging stations. The dataset has 33 columns, including session start and end dates, charging duration, total connection duration, energy delivered, station information, port and plug details, and charging fees.

## Main Question and Objectives

Our main research question is:

> How do time, location, and session characteristics relate to electric vehicle charging-station usage in Palo Alto?

We plan to investigate the following questions:

1. At what times and on which days are charging stations used most?
2. How has charging activity changed over time?
3. What is the relationship between charging duration and energy delivered?
4. Which stations have the highest usage and longest idle times?
5. How does weekday usage differ from weekend usage?
6. Are there seasonal charging patterns?
7. How often do vehicles remain connected after charging is complete?

Our hypothesis is that charging demand will be higher during weekday and daytime hours. We also expect charging duration and energy delivered to have a positive relationship, although long connection times may include significant idle time.

## Methods, Tools, and Approaches

We will use Python and Jupyter Notebook to complete the analysis. We plan to use pandas and NumPy for data cleaning, Matplotlib and Seaborn for visualizations, SciPy for statistical analysis, and scikit-learn for optional clustering.

Our process will include inspecting and cleaning the data, converting date and duration fields, creating time-related and idle-time variables, calculating descriptive statistics, comparing stations and time periods, and presenting the findings with charts and tables.

## Expected Outcome

We expect the project to identify peak charging periods, heavily used stations, locations with high idle times, and relationships among charging duration, connection duration, and energy consumption. Because the dataset is observational, we will describe associations without making unsupported causal claims.

## Project Repository

https://github.com/Noorulislam1/Data-Science-Project-
