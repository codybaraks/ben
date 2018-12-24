from flask import Flask, render_template,request,redirect,flash,url_for
import mysql.connector as connector

db = connector.connect(host="localhost", user="root", passwd="root", database="client")

app = Flask(__name__,template_folder='templates')


@app.route('/')
def hello_world():
    return redirect(url_for('contact'))

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        print(name, email, password)
        cursor = db.cursor()
        sql = "INSERT INTO `ben`(`name`, `email`, `password`) VALUES (%s,%s,%s)"
        val = (name, email, password)
        cursor.execute(sql, val)
        db.commit()
        flash("saved in database")
        redirect(url_for('show_contact'))
    return render_template('form.html')

@app.route('/show_contact')
def show_users():
    cursor = db.cursor()
    sql = "SELECT * FROM ben"
    cursor.execute(sql)
    ben = cursor.fetchall()
    return render_template('show_contact.html', ben=ben)

@app.errorhandler(404)
def error_page(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
