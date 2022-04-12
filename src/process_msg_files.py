#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Text, List, Dict

import extract_msg
import os
import re


def clean(text:Text) -> Text:
    """
        cleans the text
    """
    try:
        text = re.sub("\n+", " ", text)
        text = re.sub("\r+", " ", text)
        text = re.sub("\s+", " ", text)
        return text
    except:
        return text

def process(file_path : Text) -> Dict[Text, Text]:
    """
        processes the .msg file
    """
    response = {
        "body" : "",
        "subject" : "",
        "received_data" : "",
        "sender" : ""
    }
    try:
        msg = extract_msg.Message(file_path)
        response["body"] = clean(msg.body)
        response["subject"] = clean(msg.subject)
        response["sender"] = msg.sender
        response["date"] = msg.date
        return response
    except:
        return response

