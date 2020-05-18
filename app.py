from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from forms import RegistrationForm, LoginForm
from werkzeug import generate_password_hash, check_password_hash
import  cv2, time, os




#Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','XYZ')

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/jannat/Desktop/WEBAPPDESCRIPTION/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.password})"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    form = RegistrationForm()
    #video = cv2.VideoCapture(0)
    #check, frame = video.read()
    #key = cv2.waitKey(1)
    #cv2.imshow("Capturing", frame)
    #image = cv2.imwrite('vvg.png', video)
    #video.release()
    #cv2.destroyAllWindows()
    return render_template('about.html', title='About', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        my_user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        
        db.session.add(my_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
        

    


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        somevisitor = User.query.filter_by(email=form.email.data).first()
        if somevisitor:
            if  check_password_hash(somevisitor.password, form.password.data):
                return redirect(url_for('about'))
        return '<h1> invalid username or password </h1>'
       
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

#app.debug = True
    #app.run()


#db.session.rollback()
#flash('Error generating contact ', 'danger')

    #-------------------------------------------------------------
    #sss = INSERT INTO user (username, email, password) VALUES('{form.username.data}', '{form.email.data}', '{form.password.data}')
    #us = User(username='{form.username}',email='{form.email.data}',password='{form.password.data}')
    #db.session.add(sss)
    #db.session.commit()
    #----------------------------------------------------------------
     #description = request.form.get('username')
     #test_name = request.form.get('password')
    #----------------------------------------------------------------
     #conn = sqlite3.connect(DATABASE)
    #cur = conn.cursor()
    #cur.execute(sql, (description, test_name))
    #-------------------------------------------------------------------------------
##    # return  '<h1>' + form.username.data + '' + form.email.data + ' ' + form.password.data + '</h1>'
##    #-------------------------------------------------------------------------------------------
##     if form.email.data == 'yes@gmail.com' and form.password.data == 'notyet':
##            flash('You have been logged in!', 'success')
##            return redirect(url_for('home'))
##        else:
##            flash('Login Unsuccessful. Please check username and password', 'danger')
##    
##    
##
