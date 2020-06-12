from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()
cur.execute("SELECT * FROM pet")


@app.route('/api/pet')
def fetchPets():
    conn = psycopg2.connect("dbname=pet_hotel")
    cur = conn.cursor()
    result = cur.execute("SELECT * FROM pet")
    return result



if __name__ == "__main__":
    app.run(debug=True)
