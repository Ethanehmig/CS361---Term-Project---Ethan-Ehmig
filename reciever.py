# Author: Ethan Ehmig
# Assignment 9 

import socket
import random

def get_food_dish(temperature):
    if temperature < 80:
        return "Salad"
    elif 80 <= temperature < 100:
        return random.choice(["Caprese Salad", "Greek Salad", "Caesar Salad"])
    elif 100 <= temperature < 120:
        return random.choice(["Grilled Chicken", "Teriyaki Chicken", "Lemon Herb Chicken"])
    elif 120 <= temperature < 140:
        return random.choice(["Pasta Carbonara", "Spaghetti Bolognese", "Alfredo Pasta"])
    elif 140 <= temperature < 160:
        return random.choice(["Vegetable Stir-Fry", "Tofu and Broccoli", "Sesame Noodles"])
    elif 160 <= temperature < 180:
        return random.choice(["Baked Ziti", "Lasagna", "Eggplant Parmesan"])
    elif 180 <= temperature < 200:
        return random.choice(["Baked Salmon", "Grilled Trout", "Lemon Dill Salmon"])
    elif 200 <= temperature < 220:
        return random.choice(["Beef Stew", "Pot Roast", "Beef and Broccoli"])
    elif 220 <= temperature < 240:
        return random.choice(["Chicken Parmesan", "Chicken Marsala", "Chicken Piccata"])
    elif 240 <= temperature < 260:
        return random.choice(["Shrimp Scampi", "Garlic Butter Shrimp", "Shrimp Alfredo"])
    elif 260 <= temperature < 280:
        return random.choice(["Tofu Curry", "Vegetable Curry", "Coconut Curry"])
    elif 280 <= temperature < 300:
        return random.choice(["Barbecue Ribs", "Grilled BBQ Chicken", "Pulled Pork"])
    elif 300 <= temperature < 320:
        return random.choice(["Lobster Bisque", "Clam Chowder", "Shrimp Bisque"])
    elif 320 <= temperature < 340:
        return random.choice(["Beef Wellington", "Filet Mignon", "Ribeye Steak"])
    elif 340 <= temperature < 360:
        return random.choice(["Sushi Platter", "Sashimi Combo", "Dragon Roll"])
    elif 360 <= temperature < 380:
        return random.choice(["Paella", "Seafood Paella", "Vegetarian Paella"])
    elif 380 <= temperature < 400:
        return random.choice(["Roasted Vegetables", "Stuffed Bell Peppers", "Ratatouille"])
    else:
        return "Too hot! Maybe ice cream?"

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            temperature = float(conn.recv(1024).decode())
            food_dish = get_food_dish(temperature)
            conn.sendall(food_dish.encode())
            print(f"Sent food suggestion: {food_dish}")

start_server('localhost', 12345)
