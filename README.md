# Cyclistic-Bike-Share-Analysis
# Cyclistic Bike-Share: A Case Study in Data Analytics
### Portfolio Project

---

##  1. Business Task
The objective of this analysis is to identify behavioral differences between **annual members** and **casual riders** to help design a data-driven marketing strategy aimed at converting casual users into long-term annual members.

##  2. Data Processing & Feature Engineering
Using **Python (Pandas)**, over 5.6 million ride records across 12 months were processed:

* **Consolidated** 12 monthly datasets into a single structured dataset.
* **Removed** null values and duplicates to ensure data integrity and reliability.
* **Engineered** key features to enable robust time-series analysis:
  * `ride_length` (trip duration)
  * `day_of_week` (usage pattern)
  * `time_of_day` (morning, afternoon, evening segmentation)

##  3. Analytical Approach
The analysis focused on identifying behavioral segmentation between user types through:

* **Temporal analysis:** Hourly, daily, and seasonal trends.
* **Comparative analysis:** Casual vs. Member behavior.
* **Percentage variance:** Calculating exact mathematical differences to highlight significant shifts in usage.

---

##  4. Key Insights

###  1. Weekend Leisure Behavior
Casual riders show a **66.3% increase** in usage on Saturdays compared to weekdays, indicating strong leisure-oriented usage patterns.
> **Business Impact:** This highlights weekends as a critical conversion window where casual users are most engaged with the product.

###  2. Longer Ride Duration
Casual riders average **23.3 minutes** per ride, which is **84.5% longer** than members (12.6 minutes).
>  **Business Impact:** Casual users derive more recreational value per trip, suggesting strong potential for experience-based or weekend-only membership tiers.

###  3. Afternoon Usage Concentration
Over **43.1%** of casual rides occur between 12 PM – 5 PM, while members peak sharply during traditional commuting hours (8 AM and 5 PM).
> **Business Impact:** Marketing campaigns should heavily target afternoon leisure users rather than morning commuters.

###  4. Seasonal Sensitivity
Casual ridership drops by **59.9%** from the August summer peak to February, showing high dependency on weather conditions.
> **Business Impact:** Conversion efforts must be front-loaded before peak seasons, rather than wasting ad spend during winter decline periods.

---

##  5. Strategic Recommendations

 **1. Pre-Season Conversion Campaign**
Launch targeted membership campaigns in April–May (2–3 months before peak season) to maximize conversion during rising demand.

**2. Weekend-Focused Membership Trials**
Introduce short-term or weekend-based membership plans tailored specifically to the behaviors of leisure riders.

**3. Time-Specific Digital Advertising**
Deploy digital ads during the 12 PM – 5 PM window, emphasizing the long-term cost savings and convenience of an annual membership to active riders.
