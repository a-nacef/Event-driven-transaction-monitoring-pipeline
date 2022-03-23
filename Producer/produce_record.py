from datetime import datetime
from faker import *
import random
import json


locales = ["en_AU", "en_US", "en_GB", "en_NZ"]
countries = {"en_AU":"Australia", "en_US":"USA", "en_NZ":"New Zealand", "en_GB": "UK"}
Age_band = ["Young adult", "Adult","Senior"]
Income_band = ["Low", "Mid", "High"]
Gender = ["M", "F", "NB"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

types = ["Financial", "Training", "Software", "Legal", "Entertainment", "Marketing", "Consulting", "Legal"]

fake = Faker(locales)

def produce():
    payload = {}
    #nested dicts within an indiviual transaction
    person = {}
    event = {}
    dim_date = {}
    dim_beneficiary = {}
    timestamp = datetime.now().timestamp()
    half_bool = lambda x: x < 0.5
    #Creating a person
    loc = random.choice(locales)
    f =  fake[loc]
    person["name"] = f.name()
    person["country"] = countries[loc]
    person["age_band"] = random.choice(Age_band)
    person["Income_band"] = random.choice(Income_band)
    person["Gender"] = random.choice(Gender)
    person["Card number"] = f.credit_card_number()
    person["Account_creation_date"] = str(f.past_date())
    person["city"] = f.city()
    person["risk_score"] = random.random()
    person["credit_limit"] = round((1-person["risk_score"])*3000)
    
    payload["person"] = person

    #Filling in event facts
    payment = round(random.uniform(15.0, 40000),2)
    interest = round(random.uniform(0.03, 0.05) * payment,2)
    event["total_payment"] = payment
    event["fees_charged"] = interest + round(random.uniform(0.02,0.04) * payment,2)
    event["Interest paid"] = interest
    event["timestamp"] = timestamp
    event["total_overdrawn"] = random.choice([0,0,0, round(random.uniform(0.05, 0.3)*payment,2)]) #very hacky weighted probability there is probably a cleaner way to do this

    payload["facts"] = event

    #inferring date attributes from datetime.now
    now = datetime.now()
    dim_date["timestamp"] = timestamp
    dim_date["date"] = str(now.date())
    dim_date["Calendar_year"] = now.year
    dim_date["Month"] = now.month
    dim_date["Weekday_indicator"] = True if weekdays[now.isoweekday()-1] else False
    dim_date["Quarter"] = (now.month  // 4) + 1

    payload["date"] = dim_date
    #Filling in a random beneficiary
    dim_beneficiary["Address"] = f.address()
    dim_beneficiary["Type"] = random.choice(types)
    dim_beneficiary["Name"] = f.company()
    dim_beneficiary["Multinational_indicator"] = half_bool(random.random())
    payload["beneficiary"] = dim_beneficiary

    return payload

#DEBUG
#print(produce())
