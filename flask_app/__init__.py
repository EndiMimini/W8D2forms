from flask import Flask
app = Flask(__name__)


app.secret_key = "This is something secret! Stay quiet about this!"