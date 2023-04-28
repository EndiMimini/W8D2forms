from flask_app import app
from flask import render_template, redirect, session, request


@app.route('/create/post', methods= ['POST'])
def createPost():
    if 'username' not in session:
        return redirect('/')
    session['post'] = request.form['title']
    return redirect('/dashboard')
