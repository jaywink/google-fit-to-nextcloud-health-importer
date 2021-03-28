#!/usr/bin/env python
import json
import sys

import arrow

try:
    fit_filename = sys.argv[1]
except IndexError:
    print("Please give Google Fit weight export file as first parameter.")
    sys.exit(1)

try:
    person_id = int(sys.argv[2])
except (TypeError, IndexError):
    print("Please give Nextcloud Health person ID as second parameter.")
    sys.exit(1)

with open(fit_filename) as f:
    data = json.load(f)

if data.get("Data Source") != "raw:com.google.weight:com.google.android.apps.fitness:user_input":
    print("This doesn't look like a Google Fit app export.")
    sys.exit(1)

data = data.get("Data Points")
days = {}

for item in data:
    if item.get("dataTypeName") != "com.google.weight":
        continue

    try:
        date = arrow.get(item.get("startTimeNanos")/1000)
        date_string = date.format("YYYY-MM-DD")
        weight = round(item["fitValue"][0]["value"]["fpVal"], 1)
        now = arrow.now().format("YYYY-MM-DD HH:mm:ss")

        sql = f"insert into oc_health_weightdata (person_id, insert_time, lastupdate_time, weight, date) values (" + \
              f"{person_id}, '{now}', '{now}', {weight}, '{date_string}');"
        print(sql)
    except Exception as ex:
        print(f"Failed with a data item: {ex}")
        raise
