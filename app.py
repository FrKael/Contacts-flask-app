from flask import Flask, render_template, request,redirect ,url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

#MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#session settings
app.secret_key='mysecretkey'


@app.route('/', methods=['GET'])
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.connection.commit()
        
        flash('Contact Added Successfuly!')
        
        return redirect(url_for('Index'))

@app.route('/edit')
def edit():
    return 'EdiT'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)