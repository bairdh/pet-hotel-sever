from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()

@app.route('/api/owner', methods=['GET'])
def returnAll():
    return jsonify({ 'owner' : owner })

@app.route('/api/owner/<string:name>', methods=['GET'])
def returnOne(name):
    owner = [owner for owner in owners if owner['name'] == name]
    return jsonify({'owner' : owners[0]})


if __name__ == "__main__":
    app.run(debug=True)