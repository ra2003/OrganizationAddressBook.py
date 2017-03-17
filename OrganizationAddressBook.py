import os
import sqlite3
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'OrganizationAddressBook.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('OAB_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
