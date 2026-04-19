# Cyclistic Bike-Share: End-to-End Behavioral Analysis and Revenue Strategy

## 1. Executive Summary
This project identifies a **$3M+ revenue opportunity** by analyzing 5.6 million bike-share trips and uncovering a clear behavioral divide between recreational casual riders and efficiency-driven annual members. 

The analysis suggests that shifting from a commuter-focused model to an experience-driven strategy can effectively capture a high-value weekend segment through targeted conversion initiatives.

## 2. Business Problem
Cyclistic’s finance analysts have concluded that annual members are significantly more profitable than casual riders. The core business objective is to design marketing strategies aimed at converting existing casual riders into annual members, thereby maximizing Annual Recurring Revenue (ARR).

## 3. Data Source
* **Volume:** 5.6 Million individual ride records.
* **Format:** 12 months of historical CSV data (Year 2023).
* **Metrics:** Ride IDs, timestamps, station coordinates, bike types, and user categories.

## 4. Data Cleaning & Preparation
To ensure data integrity and prepare the dataset for Business Intelligence and Machine Learning applications, a modular Python (Pandas) pipeline was constructed.
* **Data Issues Addressed:** Handled missing values (nulls) and removed invalid system data (e.g., negative or zero-minute ride durations).
* **Feature Engineering:** Extracted high-value analytical features from raw timestamps, including `ride_length_mins`, `day_of_week`, `hour`, and categorized `time_of_day`.

## 5. Exploratory Data Analysis (EDA)
Key behavioral patterns were identified through temporal aggregation (monthly, weekly, hourly) and ride duration distribution analysis across user segments. These insights were operationalized through an interactive Power BI dashboard.

<img width="2075" height="1200" alt="Executive Overview" src="https://github.com/user-attachments/assets/2d97992e-7b37-4fda-bb36-5dba8a9e1582" />

<img width="2075" height="1200" alt="Behavior Analysis" src="https://github.com/user-attachments/assets/d62303ef-f7a0-4b31-a06a-ed9cd25a0f77" />

<img width="2075" height="1200" alt="Strategy   Action" src="https://github.com/user-attachments/assets/e9e14317-f4d5-4cec-8994-09a833dd9bb4" />

## 6. Key Behavioral Insights
These patterns indicate that **casual riders are not failed commuters, but a fundamentally different recreational segment.**
1. **The Weekend Warrior Effect:** Casual riders exhibit a 66.3% spike in usage on Saturdays and Sundays compared to weekdays, completely inverting the traditional weekday commuter model used by Members.
2. **Recreational Consumption vs. Efficiency:** Casual riders ride for an average of 23.3 minutes (84.5% longer than Members). Statistical variance (Standard Deviation) confirms Casuals use the service for unpredictable leisure, while Members use it for strict A-to-B transit.
3. **The "Hot Zone" (Spatial-Temporal Heatmap):** Matrix analysis reveals that casual rider activity is heavily concentrated during weekend afternoons (12:00 PM - 5:00 PM), indicating a clear recreational usage pattern rather than traditional commuting behavior.

## 7. Strategic Business Recommendations
Based on the data, the following Experience-Driven Strategy is recommended:
* **Action 1 (Product): Launch a "Weekend-Only" Membership.** Target the 66% weekend volume spike with a $120 annual plan that restricts weekday commuting benefits. **KPI:** Estimated $3M+ gross revenue (excluding marketing and operational costs) at a conservative 5% conversion rate.
* **Action 2 (Marketing): Precision Ad Spend.** Halt morning digital ad spend for casuals. Reallocate budget to target location-based ads strictly during the proven "Hot Zone" (Weekends, 12:00 PM - 5:00 PM). **KPI:** Increased Return on Ad Spend (ROAS).
* **Action 3 (Lifecycle): Pre-Season Campaign.** Data shows a 59.9% winter drop-off. Launch onboarding campaigns in April to capture users before the summer peak.

## 8. Technical Challenges Overcome
* **Scale:** Processing 5.6M rows required efficient programmatic concatenation and memory management in Python rather than spreadsheet tools.
* **Data Integrity:** Transforming raw, unformatted string timestamps into reliable, mathematically operable numeric features (duration, chronological sorting) required strict validation logic.

## 9. Limitations of Analysis
* **No Unique User IDs:** The dataset tracks independent rides, not individual users. Retention rates and exact ride frequency per user cannot be deterministically measured.
* **No Demographic or Financial Data:** Pricing elasticity and behavioral assumptions lack socio-economic context.
* **Inferred Seasonality:** While winter drops are severe, lack of integrated weather data means seasonality is inferred, not causally proven.

## 10. Technical Stack & Techniques
* **Python (Pandas):** Data cleaning, validation pipeline, and programmatic feature engineering.
* **Power BI & DAX:** Advanced data modeling, chronological sorting logic, and interactive dashboard design.
* **Statistical Analysis:** Variance tracking (Standard Deviation) and behavioral distribution modeling.
* **Business Strategy:** Revenue forecasting via interactive What-If Parameters.

## 11. Future Scope (Machine Learning)
The output of the Python pipeline is a strictly clean, numeric, and categorical CSV. It is fully formatted and ML-ready for future implementation of **K-Means Clustering** to algorithmically discover hidden micro-segments of users beyond the binary "Casual vs. Member" labels.
