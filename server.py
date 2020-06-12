from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()
# cur.execute("SELECT * FROM pet")

#pet get request
@app.route('/api/pet')
def fetchPets():
    conn = psycopg2.connect("dbname=pet_hotel", )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM pet")
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
