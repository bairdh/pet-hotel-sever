from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()
# cur.execute("SELECT * FROM pet")

@app.route('/add_pet', methods=['POST'])
def addPet():
    print('In Pets!')
    try:
        req = request.get_json()
        name = req.get('pet_name')
        breed = req.get('pet_breed')
        color = req.get('pet_color')
        print(name, breed, color)
        query = "INSERT INTO pet (name, breed, color, owner_id, checked_in) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(query, (name, breed, color, 2, False))
        conn.commit()
        return "hello"
    except Exception as err:
        print('ERROR in POST:', err)
        return 'Failed'


if __name__ == "__main__":
    app.run(debug=True)