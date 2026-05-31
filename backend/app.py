from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
import os

app = Flask(__name__)
CORS(app)

# MySQL Connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12943@a',
    database='analytics_dashboard'
)

# Home Route
@app.route('/')
def home():
    return "Cloud Analytics Dashboard Backend Running Successfully"

# Sales API
@app.route('/sales')
def get_sales():

    cursor = connection.cursor()

    query = "SELECT * FROM sales"

    cursor.execute(query)

    data = cursor.fetchall()

    return jsonify(data)

# Run Flask App
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)