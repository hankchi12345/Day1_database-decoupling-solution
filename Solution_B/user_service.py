# user_service.py (與 Solution_A 相同)
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def query_user_from_db(user_id):
    conn = psycopg2.connect("dbname=db_user user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = query_user_from_db(user_id)
    return jsonify({
        "id": user[0],
        "name": user[1],
        "email": user[2]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
