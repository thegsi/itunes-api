import pandas as pd
from pandas import DataFrame
import json


for o in [2888]:

    offset = o

    with open('itunes_books%d.json' % offset) as f:
        appContent = json.load(f)

    keys = appContent['results'][0].keys()

    print(keys)

    df = pd.DataFrame(columns=keys)

    for i in range(len(appContent['results'])):

        for k in keys:
            if k in appContent['results'][i]:
                appContent['results'][i][k] = str(appContent['results'][i][k])

        df = df.append(appContent['results'][i], ignore_index=True)

    df.to_csv('appstore_books%d.csv' % offset, sep=',', encoding='utf-8')
