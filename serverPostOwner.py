from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


conn = psycopg2.connect("dbname=pet_hotel")
# cur = conn.cursor()


@app.route('/owner', methods=['POST'])
def addOwner():
    cur = conn.cursor()
    try:
        sql = " INSERT INTO owner (name) VALUES ('Heather');"
        req = request.get_json()
        data = req.get("name")
        print("value %s" % data)
        cur.execute(sql,data)
        # data = cur.fetchall()
        # print (jsonify(data))
    except:
        print('ERROR in serting into owner')
        conn.rollback()
    conn.commit()
    # conn.close()

    # data = cur.fetchall()
    # results = cursor.fetchall()
    res = jsonify({'message': "success"}), 200
    return 'Success'

if __name__ == "__main__":
    app.run(debug=True)
