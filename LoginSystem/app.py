from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__) # instantiate flask objects

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') #these methods link their respective functions to the url 

@app.route('/login', methods=['GET','POST']) # creates login page, handles logic
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__': #starting server with run()
    app.run(debug=True)


