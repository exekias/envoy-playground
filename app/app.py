from flask import Flask
import socket

app = Flask('app')
@app.route('/')

def run():
    return '<h1>Hello, Server! %s</h1>' % socket.gethostname()
