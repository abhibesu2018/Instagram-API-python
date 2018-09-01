#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from yaml import load
from InstagramAPI import InstagramAPI

with open('/home/abhi/user_instagram.yaml', 'r') as f:
    doc = load(f)
api = InstagramAPI(doc["user"]["username"], doc["user"]["password"])
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")
