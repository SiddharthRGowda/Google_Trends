Reliance Infra – Google Trends Analytics Dashboard
Overview
This project tracks real‑time public search interest for Reliance Infra share price using Google Trends data.
It extracts data programmatically with Python, performs exploratory data analysis (EDA), and builds an interactive Power BI dashboard to visualize insights.

This pipeline is automated for daily refresh, making it useful for investors, analysts, and market researchers to monitor market buzz and investor sentiment.

Key Features
Automated Data Extraction – Uses pytrends to pull:

Interest over time (minute/hourly level trends)

Interest by region (state‑wise data)

Interest by categories (e.g., Finance, Business, News)

Exploratory Data Analysis (EDA):

Detects spikes and patterns in search behavior.

Highlights top performing regions and categories.

Interactive Power BI Dashboard:

Current Interest Score (latest day)

% Change vs Previous Day

Peak Search Time

Top Region

Top Category

Automated Refresh:

Daily execution via Windows Task Scheduler or Power BI Service Scheduled Refresh.

Business Questions Answered
How is public interest changing?

Are people searching more for Reliance Infra compared to yesterday?

When are people searching the most?

What times of the day see the highest spikes in searches?

Where is the interest coming from?

Which Indian states are driving the most search interest?

What categories are driving the search?

Is the search interest coming from finance, business, or other contexts?

Are there early signals for market activity?

Can spikes in search data correlate with price movement or news events?

Tech Stack
Python: pytrends, pandas, matplotlib, seaborn

Power BI: For interactive dashboard & KPIs

Automation:

Windows Task Scheduler for Python script automation

Power BI Service for scheduled dashboard refresh

Project Workflow
Data Extraction

python
Copy
Edit
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-GB', tz=330)
pytrends.build_payload(kw_list=['reliance infra share price'], timeframe='now 1-d', geo='IN')
data = pytrends.interest_over_time()
data.to_csv('reliance_trends_time.csv', index=False)
Outputs:

reliance_trends_time.csv – Interest over time

reliance_trends_region.csv – Interest by region

reliance_trends_category.csv – Interest by category

EDA & Insights

Identify peak search times.

Compare search volumes across categories.

Map top contributing states.

Power BI Dashboard

Import CSVs → Create visuals:

Line charts (interest over time)

Maps (top regions)

KPIs (Current interest, % change)

Bar charts (top categories)

Automation

Windows Task Scheduler: Runs Python script daily.

Power BI Scheduled Refresh: Auto‑updates dashboard.

How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/reliance-trends-dashboard.git
Install dependencies:

bash
Copy
Edit
pip install pandas pytrends matplotlib seaborn
Run the script:

bash
Copy
Edit
python Reliance_Infra.py
Open Power BI and load the CSV files.
