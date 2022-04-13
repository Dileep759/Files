#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def templatize(results, file_name):
    excel = pd.read_excel("DXC MasterTemplate.xlsx")
    excel.fillna('', inplace=True)
    try:
        entity_template_mapping = {
            "insured" : 17,
            "Project_Name" : 19,
            "purchase_price" : 29,
            "broker_name" : 16,
            "date" : 21,
            "target_business" : 31,
            "contact" : 9
        }
        for key, val in results.items():
            if key in entity_template_mapping:
                index = entity_template_mapping[key]
                if not excel["OUTPUT 1"][index - 2]:
                    excel["OUTPUT 1"][index - 2] = val
                else:
                    start = 2
                    while excel[f"OUTPUT {start}"][index - 2]:
                        start += 1
                    excel[f"OUTPUT {start}"][index - 2] = val
        excel.to_excel(f"./results/{file_name.replace('msg', 'xlsx')}")
        return f"./results/{file_name.replace('msg', 'xlsx')}"
    except:
        excel.to_excel(f"./results/{file_name.replace('msg', 'xlsx')}")
        return f"./results/{file_name.replace('msg', 'xlsx')}"
