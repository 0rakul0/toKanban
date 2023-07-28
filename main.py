from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    df = pd.read_csv(r'./info.csv')
    lista = df.to_dict()
    return dict(lista)


