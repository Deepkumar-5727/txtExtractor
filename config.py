#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "23011537"))
    API_HASH = os.environ.get("API_HASH", "cd59a9fc8cbdca6ae2b405f149cc3c8a")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5389632871")
