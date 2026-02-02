#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8450492472:AAE1f9y5epvaQYjxMIRXlPKdbE5P8STHaUk")
    API_ID = int(os.environ["API_ID", 30560523]
    API_HASH = os.environ["API_HASH", "17ab58948bc24d85d961a39e058478a2"]
    AUTH_USERS = "7834875502"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://mpsystem05:ZzYGIZ0a4PCUQkKm@cluster0.eppygqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
