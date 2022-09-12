import random
numbers = [12, 4, 6, 83]

def generate():
    number = random.choice(numbers)
    return f"<h1>{number}</h1>"
