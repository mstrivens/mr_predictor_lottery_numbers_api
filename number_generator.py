import random
import requests
import csv

import pandas as pd

numbers = [12, 4, 6, 83]

CSV_URL = "https://www.national-lottery.co.uk/results/euromillions/draw-history/csv"

def generate():
    number = random.choice(numbers)
    return f"<h1>{number}</h1>"

def api_call():
    numbersArray = []
    with requests.get(CSV_URL, stream=True) as r:
        print(csv.reader(r))
        lines = (line.decode('utf-8') for line in r.iter_lines())
        for row in csv.reader(lines):
            numbersArray.append(row)
            data = numbersArray[1: -1]
        df = pd.DataFrame(data = data,
                  columns = numbersArray[0])
        # print(df)
        table = df.to_html()
        print(table)
        return table

api_call()

    # text = json.dumps(response.json(), sort_keys=True, indent=4)
    # return f"<h1>{response.status_code}</h1>"
