from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify,json
from data import Articles
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
app = Flask(__name__)
# mysql -u root -p
# GRANT ALL ON root.* To 'root'@'localhost' IDENTIFIED BY '123456';
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_PASSWORD'] = '2468@HitMan'
app.config['MYSQL_DB'] = 'testflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)
app.config['JSON_ADD_STATUS'] = False
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'
Articles = Articles()

json = FlaskJSON(app)
# Index
@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')


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

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
       # password = sha256_crypt.encrypt(str(form.password.data))
        password = sha256_crypt.encrypt(str(form.password.data))
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
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
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
    result = cur.execute("SELECT * FROM users  ")
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
@app.route('/servlist')
@is_logged_in
def servlist():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM ServList")

    articles = cur.fetchall()

    if result > 0:
        return render_template('servlist.html', articles=articles)
    else:
        msg = 'No service Found'
        return render_template('servlist.html', msg=msg)
    # Close connection
    cur.close()
# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM PatientList ")

    patients = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', patients=patients)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()
@app.route('/user')
@is_logged_in
def user():
    return  render_template('user.html')
# patient Form Class
class PatientForm(Form):
    PatientName = StringField('PatientName', [validators.Length(min=1, max=200)])
    Address = TextAreaField('Address', [validators.Length(min=1)])
    ServID  = TextAreaField('ServID')
# serv form class
class ServForm(Form):
    ServName = StringField('ServName', [validators.Length(min=1, max=200)])
    Price = TextAreaField('Price', [validators.Length(min=1)])

# users Form Class
class usersForm(Form):
    name = StringField(' name', [validators.Length(min=1, max=200)])
    email = TextAreaField('email', [validators.Length(min=1)])

# Add user
@app.route('/add_user', methods=['GET', 'POST'])
@is_logged_in
def add_user():
    form = usersForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data


        # Create Cursor
        cur = mysql.aboutconnection.cursor()

        # Execute
        cur.execute("INSERT INTO users( name, email) VALUES(%s, %s)",(name, email))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('users'))

    return render_template('users.html', form=form)
# Add patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    form = PatientForm(request.form)
    if request.method == 'POST' and form.validate():
        PatientName = form.PatientName.data
        Address = form.Address.data
        ServID = form.ServID.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO PatientList( PatientName, Address,ServID ,UserName) VALUES(%s,%s , %s, %s)",(PatientName, Address ,ServID , session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_patient.html', form=form)
# add serv
@app.route('/addserv', methods=['GET', 'POST'])
def addserv():
    form = ServForm(request.form)
    if request.method == 'POST' and form.validate():
        ServName = form.ServName.data
        Price = form.Price.data


        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO ServList( ServName, Price) VALUES(%s,%s )",(ServName, Price))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('addserv.html', form=form)

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

    if request.method == 'POST' and form.validate():
        PatientName = request.form['PatientName']
        Address = request.form['Address']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(PatientName)
        # Execute
        cur.execute ("UPDATE PatientList SET PatientName=%s, Address=%s WHERE id=%s",(PatientName, Address, id))
        # Commit to DBDoctors/Doctor/MDetails?id=' + $('#vpatid').val()
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Patient Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_patient.html', form=form)

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

    flash('user Deleted', 'success')

    return redirect(url_for('user'))
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

    return redirect(url_for('dashboard'))
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
