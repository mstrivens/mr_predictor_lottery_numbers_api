import random
import requests
import csv

import pandas as pd

numbers = [12, 4, 6, 83]

CSV_URL = "https://www.national-lottery.co.uk/results/euromillions/draw-history/csv"
main_balls_headers = ['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5']
lucky_balls_headers = ['Lucky Star 1', 'Lucky Star 2']

def generate():
    number = random.choice(numbers)
    return f"<h1>{number}</h1>"

def api_call():
    balls = []
    lucky_balls = []
    numbersArray = []
    with requests.get(CSV_URL, stream=True) as r:
        lines = (line.decode('utf-8') for line in r.iter_lines())
        for row in csv.reader(lines):
            numbersArray.append(row)
            data = numbersArray[1: -1]
        df = pd.DataFrame(data = data,
                  columns = numbersArray[0])
        # print(df)
        for row in df.iterrows():
            # print(row[1]['Ball 1'])
            for header in main_balls_headers:
                balls.append(row[1][header])
            for header in lucky_balls_headers:
                lucky_balls.append(row[1][header])
                # balls.append(row[1]['Ball 1'])
        # dataFrameRow
        print("BALLS", balls)
        print("LUCKY BALLS", lucky_balls)

        table = df.to_html()
        return table

api_call()

    # text = json.dumps(response.json(), sort_keys=True, indent=4)
    # return f"<h1>{response.status_code}</h1>"
