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
    conn = psycopg2.connect("dbname=pet_hotel")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT owner.name as owner_name, pet.name, pet.breed, pet.color, pet.checked_in, pet.owner_id FROM pet JOIN owner ON pet.owner_id=owner.id")
    return jsonify(cur.fetchall())

#owner get request
@app.route('/api/owner')
def fetchOwner():
    conn = psycopg2.connect("dbname=pet_hotel", )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM owner")
    return jsonify(cur.fetchall())


if __name__ == "__main__":
    app.run(debug=True)
