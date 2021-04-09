from flask import Flask, render_template , request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = False

# db = SQLAlchemy(app)

# class data(db.Model):
#     sno = db.Column()

# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#         return home()


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def revisit():
    return render_template('revisit.html')

@app.route('/inference')
def inferencing():
    return render_template('inference.html')

if __name__ == '__main__':
    app.run(debug=True)
