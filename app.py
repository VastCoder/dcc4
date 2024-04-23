from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="dcc4"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    cursor_ebred = mydb.cursor(dictionary=True)
    cursor_ebpur = mydb.cursor(dictionary=True)
    
    sql_ebred = "SELECT * FROM ebred WHERE `Bond Number` LIKE %s OR `Date of Encashment` LIKE %s OR `Name of the Political Party` LIKE %s OR `Account no. of Political Party` LIKE %s OR Prefix LIKE %s OR Denominations LIKE %s OR `Pay Branch Code` LIKE %s OR `Pay Teller` LIKE %s"
    cursor_ebred.execute(sql_ebred, (f"%{query}%",)*8)
    results_ebred = cursor_ebred.fetchall()
    
    sql_ebpur = "SELECT * FROM ebpur WHERE `Bond Number` LIKE %s OR `Journal Date` LIKE %s OR `Name of the Purchaser` LIKE %s OR `Issue Branch Code` LIKE %s OR `Issue Teller` LIKE %s"
    cursor_ebpur.execute(sql_ebpur, (f"%{query}%",)*5)
    results_ebpur = cursor_ebpur.fetchall()
    
    cursor_ebred.close()
    cursor_ebpur.close()
    
    return render_template('index.html', results_ebred=results_ebred, results_ebpur=results_ebpur)

if __name__ == '__main__':
    app.run(debug=True)
