# Bellabeat Data Analysis Case Study

**Author:** Nikodem Kijas  
**Tools Used:** Python (Pandas, Matplotlib, Seaborn)

## Project Overview

This project is a data analysis case study focused on analyzing smart device usage data to find insights and provide strategic recommendations for Bellabeat.

## Key Steps in the Analysis

1. **Data Cleaning & Transforming:** Formatted datetime columns, dropped duplicates, and normalized data.
2. **Feature Engineering:** Engineered new metrics such as `DayOfWeek`, `TotalWearMinutes`, `WearsAllDay`, and sleep quality indicators like `AwakeInBedMinutes`.
3. **Data Visualization:** Created impactful charts using Seaborn and Matplotlib to highlight engagement drops, daily intensity, sleep issues, and METs zones.

## Key Insights Discovered

- **Device Usage:** Almost half of the users (45.3%) do not wear the band all day, with the average wear time being 19 hours and 24 minutes.
- **Activity Patterns:** There is a visible drop in activity on Tuesdays and Sundays. During the day, there are two activity peaks: a smaller one at 12:00 and a larger one around 19:00.
- **Sleep Quality:** 71% of the recorded nights show that users fail to get the recommended 8 hours of sleep. Users spend an average of 32 minutes awake in bed, with some struggling with much bigger problems.
- **Workout Intensity:** While steps and calories correlate, many users burn a high number of calories despite taking very few steps, indicating non-stepping workouts. The vast majority of active time is spent in the lightly or fairly active zones, with the very active zone representing only a tiny fraction of the routine.

## Strategic Recommendations for Bellabeat

Based on the data, here are 4 main areas for improvement:

1. **Hardware Improvements:** Investigate the root cause of the daily drop-off by prioritizing battery life and redesigning the strap for seamless, 24/7 wearability.
2. **Precise Notifications:** Send a notification at 12:00 PM to remind users to stretch, and around 6:30 PM to motivate them for a main workout. Suggest easy goals on Tuesdays and Sundays to maintain the habit.
3. **Sleep Education and Support:** Add an educational section on healthy habits, a "Wind Down" mode to help users prepare for bed, and a Smart Alarm to detect sleep and wake users after 8 hours.
4. **Revamping Gamification:** Instead of just tracking 10,000 steps, introduce challenges based on time spent in an elevated heart rate zone to appreciate every type of sport and encourage intense physical effort.
