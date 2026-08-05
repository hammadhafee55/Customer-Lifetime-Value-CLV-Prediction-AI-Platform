

from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import joblib



model = joblib.load(
    "CLV_Model.pkl"
)



app = FastAPI(
title="CLV Prediction API"
)



class Customer(BaseModel):

    Age:int
    Gender:int
    Tenure_Months:int
    Recency_Days:int
    Frequency:int
    Monetary_Value:float
    Avg_Order_Value:float
    Orders:int
    Marketing_Channel:int




@app.get("/")
def home():

    return {

    "status":
    "CLV API Running"

    }



@app.post("/predict")


def predict(
    customer:Customer
):


    df=pd.DataFrame(
        [customer.dict()]
    )


    df["Customer_Value_Score"]=(

        df["Frequency"]*

        df["Avg_Order_Value"]

    )


    df["Purchase_Intensity"]=(

        df["Frequency"]/

        df["Tenure_Months"]

    )


    df["Recency_Score"]= (

        365 -

        df["Recency_Days"]

    )


    result=model.predict(df)


    return {

    "CLV":

    round(float(result[0]),2)

    }
