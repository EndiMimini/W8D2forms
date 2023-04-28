from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/dashboard')
    return redirect('/loginPage')

@app.route('/loginPage')
def loginPage():
    if 'username' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/login', methods= ['POST'])
def login():
    if 'username' in session:
        return redirect('/')
    
    session['username'] = request.form['username']
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/logout')
    loggedUser = session['username']
    if 'post' in session:
        postTitle = session['post']
        return render_template('dashboard.html', loggedUser = loggedUser, postTitle = postTitle)

    return render_template('dashboard.html', loggedUser = loggedUser)


@app.route('/about')
def about():
    if 'username' not in session:
        return redirect('/logout')
    return render_template('about.html', loggedUser = session['username'])



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


