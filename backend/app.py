from flask import Flask, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MySQL Connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12943@a',
    database='analytics_dashboard'
)

@app.route('/')
def home():
    return "Backend Running Successfully"

# API Route
@app.route('/sales')
def get_sales():

    cursor = connection.cursor()

    query = "SELECT * FROM sales"

    cursor.execute(query)

    data = cursor.fetchall()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)