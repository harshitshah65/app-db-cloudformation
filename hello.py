from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=<Master DB Password>
app.config['MYSQL_DATABASE_DB']='reports'
app.config['MYSQL_DATABASE_HOST']=<RDS Endpoint Adress>
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def hello_db():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from rally;")
    data = cursor.fetchall()
#    rows = []
#    for row in data:
#        rows.append(row)
#        print(row)
    #print data
    #return 'Hello, World!'
    return render_template('db.html', data = data)

if __name__ == "__main__": 
    app.run(host='0.0.0.0',ssl_context=('cert.pem', 'key.pem'))
