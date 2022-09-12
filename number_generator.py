import random
import requests
numbers = [12, 4, 6, 83]

def generate():
    number = random.choice(numbers)
    return f"<h1>{number}</h1>"

def api_call():
    response = requests.get("https://www.national-lottery.co.uk/results/euromillions/draw-history/csv")
    return f"<h1>{response.status_code}</h1>"
