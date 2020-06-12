from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=pet_hotel")
cur = conn.cursor()
# cur.execute("SELECT * FROM pet")

@app.route('/addPet', methods=['POST'])
def addPet():
    try:
        req: request.get_json()
        data = req.get('newPet')
        print(data)
        cur.execute()
        return req
    except Exception as err:
        print('ERROR in POST:', err)
        return 'Failed'


if __name__ == "__main__":
    app.run(debug=True)