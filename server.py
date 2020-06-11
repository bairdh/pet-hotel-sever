from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()
# cur.execute("SELECT * FROM pet")

@app.route('/')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)