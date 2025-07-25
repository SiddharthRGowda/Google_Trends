
# %%
from pytrends.request import TrendReq
import pandas as pd
import time
import random

# Safe wrapper for build_payload with retries and backoff
def safe_build_payload(pytrends, kw_list, timeframe, geo, cat=0, max_retries=5):
    for attempt in range(max_retries):
        try:
            pytrends.build_payload(kw_list=kw_list, timeframe=timeframe, geo=geo, cat=cat)
            return True
        except Exception as e:
            wait_time = random.randint(15, 30) * (attempt + 1)  # exponential backoff
            print(f"[Retry {attempt+1}/{max_retries}] Error: {e}. Waiting {wait_time}s before retrying...")
            time.sleep(wait_time)
    raise Exception("Max retries reached. Google is blocking the requests.")

# ---------- Setup ----------
pytrends = TrendReq(hl='en-GB', tz=330)
keywords = ['reliance infra share price']
timeframe = 'now 7-d'  # Last 7 days
geo = 'IN'

# ---------- Interest over time ----------
safe_build_payload(pytrends, keywords, timeframe, geo)
interest_over_time = pytrends.interest_over_time()
if 'isPartial' in interest_over_time.columns:
    interest_over_time = interest_over_time.drop(columns=['isPartial'])
interest_over_time.reset_index(inplace=True)

# ---------- Interest by region ----------
time.sleep(random.randint(10, 20))  # Delay to avoid immediate next request
safe_build_payload(pytrends, keywords, timeframe, geo)
interest_by_region = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True).reset_index()

# ---------- Interest by categories ----------
categories = {
    0: 'All Categories',
    34: 'Arts & Entertainment',
    3: 'Business',
    5: 'Computers & Electronics',
    7: 'Finance',
    13: 'Sports'
}

category_data = []
for cat_id, cat_name in categories.items():
    for attempt in range(3):  # retry 3 times per category
        try:
            safe_build_payload(pytrends, keywords, timeframe, geo, cat=cat_id)
            df = pytrends.interest_over_time().drop(columns='isPartial', errors='ignore').reset_index()
            df['Category'] = cat_name
            category_data.append(df)
            print(f"Fetched category: {cat_name}")
            break
        except Exception as e:
            print(f"Error fetching category {cat_name} (attempt {attempt+1}): {e}")
            time.sleep(10 * (attempt + 1))
    time.sleep(random.randint(10, 20))  # random delay between categories

interest_by_category = pd.concat(category_data, ignore_index=True)

# ---------- Save to CSV ----------
interest_over_time.to_csv(r'C:\Users\siddh\.jupyter\Trends Data\reliance_trends_time.csv', index=False)
interest_by_region.to_csv(r'C:\Users\siddh\.jupyter\Trends Data\reliance_trends_region.csv', index=False)
interest_by_category.to_csv(r'C:\Users\siddh\.jupyter\Trends Data\reliance_trends_category.csv', index=False)

print("Data extraction complete.")
print("\nInterest Over Time sample:")
print(interest_over_time.head())
print("\nInterest by Region sample:")
print(interest_by_region.head())
print("\nInterest by Category sample:")
print(interest_by_category.head())



