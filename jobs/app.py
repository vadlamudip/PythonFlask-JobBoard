import sqllite3
from flask import Flask, render_template, g

PATH = 'db/jobs.sqllite'
app = Flask(__name__)


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqllite3.connect(PATH)
    connection.row_factory = sqllite3.row
    return connection

def execute_sql(sql, values=(), commit = True, single = True):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
                    
@app.teardown_appcontext                    
def close_connection():
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
