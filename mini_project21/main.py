from flask import Flask, render_template , request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('signup.html')

@app.route('/create_project')
def create_project():
    return render_template('create_project.html')

@app.route('/revisit')
def revisit():
    return render_template('revisit.html')

@app.route('/inference')
def inferencing():
    return render_template('inference.html')

if __name__ == '__main__':
    app.run(debug=True)
