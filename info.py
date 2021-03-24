import json
import gzip
import pandas as pd

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)
    
def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    print("parseLine")
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')
df = getDF('../Data/Phones_5.json.gz')
df.to_pickle("./dataframe/Phones_5.pkl")