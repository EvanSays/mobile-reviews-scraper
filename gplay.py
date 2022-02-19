import os
import pandas as pd
import numpy as np

from google_play_scraper import app, Sort, reviews_all
from pprint import pprint
from datetime import date

print("Starting...Scraping Gplay")

reviews = reviews_all(
  'com.cerebral.cerebral',
  sleep_milliseconds=0,
  sort=Sort.NEWEST,
)

today = date.today()
df = pd.DataFrame(np.array(reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
df2.to_csv(f'Data/{today}-gplay.csv', index=False)
df2.head()