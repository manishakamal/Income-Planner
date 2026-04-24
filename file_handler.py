# file_handler.py

import os

DATA_FILE = "profile.txt"

def save_data(data):
    with open(DATA_FILE, "w") as f:
        for key, value in data.items():
            f.write(key + "=" + str(value) + "\n")

def load_data():
    if not os.path.exists(DATA_FILE):
        return None
    data = {}
    with open(DATA_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                data[key] = value
    return data
