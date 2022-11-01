import random
import requests
import csv
import json

import pandas as pd

CSV_URL = "https://www.national-lottery.co.uk/results/euromillions/draw-history/csv"
main_balls_headers = ['Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5']
lucky_balls_headers = ['Lucky Star 1', 'Lucky Star 2']

def return_best_numbers():
    balls = []
    lucky_balls = []
    ball_counter = {}
    lucky_ball_counter = {}
    best_numbers = []
    best_lucky_balls = []
    with api_call(CSV_URL) as r:
        df = return_dataframe_from_api(r)
        extract_numbers_from_dataframe(balls, lucky_balls, df)
        countBallFrequency(balls, ball_counter)
        countBallFrequency(lucky_balls, lucky_ball_counter)
        priorityQueue(ball_counter, best_numbers, 5)
        priorityQueue(lucky_ball_counter, best_lucky_balls, 2)
        return json.dumps({"best_numbers": best_numbers,
                "best_lucky_balls": best_lucky_balls
                })

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

def priorityQueue(ball_count_obj, best_balls_arr, num_balls_to_ret):
    for key in ball_count_obj:
        if len(best_balls_arr) < num_balls_to_ret:
            best_balls_arr.append(key)
        else:
            for i in reversed(range(len(best_balls_arr))):
                if ball_count_obj[best_balls_arr[i]] < ball_count_obj[key]:
                    best_balls_arr.insert(i, key)
                    best_balls_arr.pop()
                    break;
    return best_balls_arr

def countBallFrequency(ball_arr, ball_count_obj):
    for number in ball_arr:
        if number not in ball_count_obj:
            ball_count_obj[number] = 1
        else:
            ball_count_obj[number] += 1
    return ball_count_obj


return_best_numbers()
