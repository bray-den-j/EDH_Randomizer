from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/randomizer', methods=['POST'])
def randomizer():
    # Run the script to select a random creature
    result = select_random_creature("legendary_filtered.csv")
    return render_template('result.html', result=result)

def select_random_creature(csv_file):
    # Read the CSV file and extract creature names
    creatures = []
    with open(csv_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            creatures.append(row["name"])

    # Select a random creature from the list
    random_creature = random.choice(creatures)
    return random_creature

if __name__ == '__main__':
    app.run(debug=True)