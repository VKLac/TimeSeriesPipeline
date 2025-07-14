#%%
import pandas as pd
import numpy as np
from datetime import datetime
import requests

from scripts.functions import scrape_data_indicators
from sqlalchemy import create_engine

# %%
urls = ["https://www.gov.br/receitafederal/pt-br",
        "https://datasus.saude.gov.br/"]

data_monitoring = []

for url in urls:

    request = requests.get(url)

    status = request.status_code
    latency = request.elapsed.total_seconds()
    response_url = 1 if request.url == url else 0  

    data_monitoring.append({
        "url":url,
        "status":status,
        "latency":latency,
        "response":response_url,
        "timestamp": datetime.now()

    })

data_monitoring = pd.DataFrame(data_monitoring)

engine = create_engine("postgresql://vilacerda:aiops123@localhost:5432/monitoramento")

data_monitoring.to_sql(
    name = "tracking_websites",
    con = engine,
    if_exists = "append",
    index = False
)


