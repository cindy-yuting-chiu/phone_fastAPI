import pandas as pd

url = 'https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-cities.csv?raw=true'
df = pd.read_csv(url)

df.rename(columns ={'201':'area_code','Bayonne':'City','New Jersey':'State', 'US':'Country','40.66871':'Long', '-74.11431':'Lat' })

def area_code(num):
    area = int(num[0:3])
    print(area)
    return df.loc[df['area_code']== area ,['State']]['State'].unique().tolist()