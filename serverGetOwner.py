from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()

@app.route('/owner', methods=['GET'])
def returnAll():
    return jsonify({ 'owner' : owner })

@app.route('/owner/<string:name>', methods=['GET'])
def returnOne(name):
    owner = [owner for owner in owners if owner['name'] == name]
    return jsonify({'owner' : owners[0]})


if __name__ == "__main__":
    app.run(debug=True)