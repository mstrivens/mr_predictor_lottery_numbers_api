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

def return_best_numbers():
    balls = []
    lucky_balls = []
    ball_counter = {}
    with api_call(CSV_URL) as r:
        df = return_dataframe_from_api(r)
        extract_numbers_from_dataframe(balls, lucky_balls, df)
        print("BALLS", balls)
        print("LUCKY BALLS", lucky_balls)
        for number in balls:
            if number not in ball_counter:
                ball_counter[number] = 1
            else:
                ball_counter[number] += 1
        best_numbers = []
        print("BALL COUNTER", ball_counter)
        for key in ball_counter:
            if len(best_numbers) < 6:
                best_numbers.append(key)
            elif ball_counter[best_numbers[5]] < ball_counter[key]:
                best_numbers[5] = key
            else:
                for i in range(len(best_numbers)):
                    if ball_counter[best_numbers[i]] < ball_counter[key]:
                        best_numbers[i] = key
                        break;
        table = df.to_html()
        return table

def api_call(url):
    return requests.get(url, stream=True)

def return_dataframe_from_api(response):
    numbers_array = []
    lines = (line.decode('utf-8') for line in response.iter_lines())
    for row in csv.reader(lines):
        numbers_array.append(row)
        data = numbers_array[1: -1]
    return pd.DataFrame(data = data,
              columns = numbers_array[0])

def extract_numbers_from_dataframe(balls, lucky_balls, df):
    for row in df.iterrows():
        for header in main_balls_headers:
            balls.append(row[1][header])
        for header in lucky_balls_headers:
            lucky_balls.append(row[1][header])

def hash_key(hash):
    return hash['']

return_best_numbers()

    # text = json.dumps(response.json(), sort_keys=True, indent=4)
    # return f"<h1>{response.status_code}</h1>"
