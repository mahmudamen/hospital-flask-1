from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify,json
#from data import Articles
from wtforms import form, TextField, DecimalField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask_bootstrap import Bootstrap
from flask_json import FlaskJSON, JsonError, json_response, as_json
#import MySQLdb as MySQL
from flask_mysqldb import MySQL
import hashlib as hash
#from flaskext.mysql import MySQL

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import decimal
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "dontell"
# mysql -u root -p
# GRANT ALL ON root.* To 'root'@'localhost' IDENTIFIED BY '123456';
# Config MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)
app.config['JSON_ADD_STATUS'] = False
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'
#Articles = Articles()

json = FlaskJSON(app)
# Index
@app.route('/')
def index():
    return render_template('home.html')
# About
@app.route('/about', methods=['GET', 'POST'])
def about():
    form = PatientForm(request.form)
    # app.logger.info(help(form))
    if request.method == 'POST':# and form.validate():
        PatientName = form.PatientName.data

        app.logger.info(PatientName)
        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO xpatient( PatientName) VALUES(%s )", (PatientName))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Patient  Created', 'success')

        return redirect(url_for('Patient'))

    return render_template('about.html', form=form)
# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
#
# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        #password = hash.sha256(str(form.password.data)).hexdigest()

        app.logger.info(password)
        app.logger.info(form.password.data)
        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            #if str(hash.sha256(password_candidate).hexdigest()) == str(password):
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboardd'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap
@app.route('/tab',methods=['GET', 'POST'])
@is_logged_in
def tab():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM users")
    articles = cur.fetchall()
    if result > 0:
        return jsonify(data = articles)

    else:
        msg = 'No users  Found'
        return render_template('users.html', msg=msg)
    # Close connection
    cur.close()
@app.route('/users')
@is_logged_in
def users():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM users")

    articles = cur.fetchall()

    if result > 0:
        return render_template('users.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('users.html', msg=msg)
    # Close connection
    cur.close()
@app.route('/serv')
@is_logged_in
def serv():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM ServList")

    articles = cur.fetchall()

    if result > 0:
        return render_template('serv.html', articles=articles)
    else:
        msg = 'No service Found'
        return render_template('serv.html', msg=msg)
    # Close connection
    cur.close()
# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
# Dashboard2
@app.route('/dashboardd')
@is_logged_in
def dashboardd():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM PatientList")

    patients = cur.fetchall()

    if result > 0:
        return render_template('dashboardd.html', patients=patients)
    else:
        msg = 'No Patient Found'
        return render_template('dashboardd.html', msg=msg)
    # Close connection
    cur.close()
@app.route('/patient')
@is_logged_in
def patient():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM PatientList")

    patients = cur.fetchall()

    if result > 0:
        return render_template('patient.html', patients=patients)
    else:
        msg = 'No patient Found'
        return render_template('patient.html', msg=msg)
    # Close connection
    cur.close()
@app.route('/user')
@is_logged_in
def user():
    return  render_template('user.html')
# patient Form Class
class PatientForm(Form):
    PatientName = StringField(' ', [validators.Length(min=1, max=200)])
    Address = StringField(' ', [validators.Length(min=1)])
    ServID = SelectField(' ')
    ServName =StringField(' ')
    Price = DecimalField(' ')
# serv form class
class ServForm(Form):
    ServName = StringField('', [validators.Length(min=3)])
    Price = StringField('' )
# users Form Class
class usersForm(Form):
    name = StringField(' ', [validators.Length(min=1, max=200)])
    email = StringField(' ', [validators.Length(min=1)])

# Add user
@app.route('/add_user', methods=['GET', 'POST'])
@is_logged_in
def add_user():
    form = usersForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data


        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO users( name, email) VALUES(%s, %s)",(name, email))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('users'))

    return render_template('users.html', form=form)
# Add patient with bootstrap
@app.route('/addpat', methods=['GET', 'POST'])
@is_logged_in
def addpat():
    form = PatientForm(request.form)
    if request.method == 'POST' : # and form.validate():
        PatientName = form.PatientName.data
        Address = form.Address.data
        ID = form.ServID.data
        ServName = form.ServName.data
        Price = form.ServName.data

        app.logger.info(PatientName)
        app.logger.info(Address)
        app.logger.info(Price)
        app.logger.info(ServName)
        app.logger.info(Price)
        # Create Cursor
        cur = mysql.connection.cursor()
        # Execute
        cur.execute("SELECT ServName FROM ServList WHERE id = %s", [ID])

        ServName = cur.fetchall()
        ServName = ServName[0]['ServName']
        cur.execute('SELECT Price FROM ServList WHERE id = %s', [ID])
        Price = cur.fetchall()
        Price = Price[0]['Price']
        cur.execute("INSERT INTO PatientList( PatientName,Address,ServID,ServName,Price) VALUES(%s,%s,%s,%s,%s)",
                    (PatientName, Address, ID, ServName, Price))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Patient Created', 'success')

        return redirect(url_for('dashboardd'))
    else:
        flash('Patient Created', 'danger')

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT ID , ServName FROM ServList")
    serv = cur.fetchall()
    app.logger.info(type(serv))
    app.logger.info(serv)
    app.logger.info(serv[0]['ServName'])
    return render_template('addpat.html', form=form, serv=serv)

# Add patient with bootstrap
@app.route('/add_patient', methods=['GET', 'POST'])
@is_logged_in
def add_patient():
    form = PatientForm(request.form)
    if request.method == 'POST' : #and form.validate():
        PatientName = form.PatientName.data
        Address = form.Address.data
        ServID = form.ServID.data
        ServName=form.ServName.data
        Price = form.Price.data

        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("SELECT ServName FROM ServList WHERE id = %s", [ServID])

        ServName = cur.fetchall()
        ServName = ServName[0]['ServName']
        cur.execute('SELECT Price FROM ServList WHERE id = %s', [ServID])
        Price = cur.fetchall()
        Price = Price[0]['Price']
        # Execute
        cur.execute("INSERT INTO PatientList( PatientName, Address,ServID ,ServName,Price,UserName) VALUES(%s,%s ,%s,%s, %s, %s)",(PatientName, Address ,ServID ,ServName,Price ,session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Patient Created', 'success')

        return redirect(url_for('dashboardd'))
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT ID , ServName FROM ServList")
    serv = cur.fetchall()
    app.logger.info(type(serv))
    app.logger.info(serv)
    app.logger.info(serv[0]['ServName'])

    return render_template('add_patient.html', form=form, serv=serv)
# add serv
@app.route('/add_servList', methods=['GET', 'POST'])
def add_servList():
    form = ServForm(request.form)
    # app.logger.info(help(form))
    if request.method == 'POST' and form.validate():
        ServName = form.ServName.data
        Price = form.Price.data
        app.logger.info(Price)
        app.logger.info(ServName)
        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO ServList( ServName, Price) VALUES(%s,%s )",(ServName, Price))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Service  Created', 'success')

        return redirect(url_for('serv'))

    return render_template('add_servList.html', form=form)
# Edit user
@app.route('/edit_user/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_user(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM users WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = usersForm(request.form)

    # Populate article form fields
    form.name.data = article['name']
    form.email.data = article['email']

    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(email)
        # Execute
        cur.execute ("UPDATE users SET name=%s, email=%s WHERE id=%s",(name, email, id))
        # Commit to DBDoctors/Doctor/MDetails?id=' + $('#vpatid').val()
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('users'))

    return render_template('edit_user.html', form=form)
# Edit delete patient
@app.route('/edit_patient/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_patient(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM PatientList WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = PatientForm(request.form)

    # Populate article form fields
    form.PatientName.data = article['PatientName']
    form.Address.data = article['Address']
    form.ServID.data = article['ServID']
    form.Price.data = article['Price']

    if request.method == 'POST' and form.validate():
        PatientName = str(request.form['PatientName'])
        Address = str(request.form['Address'])
        ServID = str(request.form['ServID'])
        Price = str(request.form['Price'])

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(PatientName)
        # Execute
        cur.execute ("UPDATE Patient SET PatientName=%s , Address=%s , ServID=%s,Price=%s WHERE id=%s",(PatientName,Address,ServID,Price, id))
        # Commit to DBDoctors/Doctor/MDetails?id=' + $('#vpatid').val()
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Patient Updated', 'success')

        return redirect(url_for('patient'))
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT ID , ServName FROM ServList")
    serv = cur.fetchall()
    app.logger.info(type(serv))
    app.logger.info(serv)
    app.logger.info(serv[0]['ServName'])

    return render_template('edit_patient.html', form=form )
@app.route('/edit_item/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_item(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM ItemList WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = itemform(request.form)

    # Populate article form fields
    form.ItemName.data = article['ItemName']
    form.Price.data = article['Price']

    if request.method == 'POST' and form.validate():
        ItemName = request.form['ItemName']
        Price = request.form['Price']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(ItemName)
        # Execute
        cur.execute("UPDATE ItemList SET ItemName=%s, Price=%s WHERE id=%s", (ItemName, Price, id))
        # Commit to DBDoctors/Doctor/MDetails?id=' + $('#vpatid').val()
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Item Updated', 'success')

        return redirect(url_for('item'))

    return render_template('edit_item.html', form=form)
# Edit delete serv
@app.route('/edit_serv/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_serv(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM ServList WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = ServForm(request.form)

    # Populate article form fields
    form.ServName.data = article['ServName']
    form.Price.data = article['Price']

    if request.method == 'POST' and form.validate():
        ServName = request.form['ServName']
        Price = request.form['Price']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(ServName)
        # Execute
        cur.execute ("UPDATE ServList SET ServName=%s, Price=%s WHERE id=%s",(ServName, Price, id))
        # Commit to DBDoctors/Doctor/MDetails?id=' + $('#vpatid').val()
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('service Updated', 'success')

        return redirect(url_for('serv'))

    return render_template('edit_serv.html', form=form)
# Delete user
@app.route('/delete_user/<string:id>', methods=['POST'])
@is_logged_in
def delete_user(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM users WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('serv Deleted', 'success')

    return redirect(url_for('users'))
@app.route('/delete_serv/<string:id>', methods=['POST'])
@is_logged_in
def delete_serv(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM ServList WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('serv Deleted', 'success')

    return redirect(url_for('serv'))
@app.route('/delete_patient/<string:id>', methods=['POST'])
@is_logged_in
def delete_patient(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM PatientList WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Patient Deleted', 'success')

    return redirect(url_for('dashboardd'))
@app.route('/delete_item/<string:id>', methods=['POST'])
@is_logged_in
def delete_item(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM ItemList WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('item Deleted', 'success')

    return redirect(url_for('item'))
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = itemform(request.form)
    # app.logger.info(help(form))
    if request.method == 'POST' and form.validate():
        ItemName = form.ItemName.data
        Price = form.Price.data
        app.logger.info(Price)
        app.logger.info(ItemName)
        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO ItemList( ItemName, Price) VALUES(%s,%s )", (ItemName, Price))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Item  Created', 'success')

        return redirect(url_for('item'))
    return render_template('add_item.html', form=form)
@app.route('/item')
def item():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM ItemList")

    articles = cur.fetchall()

    if result > 0:
        return render_template('item.html', articles=articles)
    else:
        msg = 'No service Found'
        return render_template('item.html', msg=msg)
    # Close connection
    cur.close()
class itemform(Form):
    ItemName = StringField('', [validators.Length(min=4, max=25)])
    Price = DecimalField('')
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
