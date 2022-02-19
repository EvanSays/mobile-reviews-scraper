from app_store_scraper import AppStore

import pandas as pd
import numpy as np
import json
from pprint import pprint

from datetime import date

print("Starting...Scraping App Store")

app = AppStore(country="us", app_name="cerebral")
app.review(how_many=1500)
app.reviews

today = date.today()
df = pd.DataFrame(np.array(app.reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
df2.to_csv(f'Data/{today}-appstore.csv', index=False)
df2.head()
