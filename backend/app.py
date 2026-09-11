from flask import Flask, jsonify

import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="database",
        database="myapp",
        user="admin",
        password="password"
    )

@app.route("/api/message")
def message():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    version = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Backend connecté à PostgreSQL",
        "database": version
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
