from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()
url = 'https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-cities.csv?raw=true'
df = pd.read_csv(url)

df = df.rename(columns ={'201':'area_code','Bayonne':'City','New Jersey':'State', 'US':'Country','40.66871':'Long', '-74.11431':'Lat' })

@app.get("/")
async def root():
    return {"message": "Input your phone number xxxxxxxxxx"}

@app.get("/phone/{num1}")
async def area_code(num1: str):
    """Return state for the given phone number"""
    num = str(num1)
    area = int(num[0:3])
    state = df.loc[df['area_code']== area ,['State']]['State'].unique().tolist()
    city = df.loc[df['area_code']== area ,['City']]['City'].unique().tolist()
    return {'state': state, 'city':city}

@app.get("/state/{st}")
async def state_code(st : str):
    """Return area code for a given state """ 
    area_code  = df.loc[df['State']== st ,['area_code']]['area_code'].unique().tolist()
    return {'area code': area_code}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
