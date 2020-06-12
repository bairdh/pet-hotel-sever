from flask import Flask, jsonify, request, make_response
import psycopg2

app = Flask(__name__)

@app.route('/owner', methods=['POST'])
def addOwner():
    conn = psycopg2.connect("dbname=pet_hotel")
    cur = conn.cursor()
    try:
        sql = "INSERT INTO owner (name) VALUES (%s);"
        req = request.get_json()
        data = req.get("name")
        print("value", data)
        cur.execute(sql, (data,))
        conn.commit()
        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)

    except Exception as err:
        print(err)
        conn.rollback()
        res = 500
        return res   


if __name__ == "__main__":
    app.run(debug=True)
