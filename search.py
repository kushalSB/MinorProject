
from flask import Flask
import json

from flask_mysqldb import MySQL



        
app = Flask(__name__) 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nest'

mysql = MySQL(app)
#is_logged_in=true
@app.route('/searchall')
def returnAll():
    
    #Database command to get all data
    cursor= mysql.connection.cursor()
    cursor.execute('''SELECT * FROM Homestay''')
    records=cursor.fetchall()

    insertObject=[]
    columnNames= [column[0] for column in cursor.description]
    for record in records:
        insertObject.append( dict( zip( columnNames , record ) ) )
    
    cursor.close()
    return (json.dumps(insertObject))
    #Python Technique to make list of dictionary using key as Coloumn name in Database
   

@app.route('/searchlocation/<location>')
def searchLocation(location):

    cursor=mysql.connection.cursor()
    cursor.execute(""" SELECT * FROM Homestay WHERE Homestay_location='{0}'""".format(location))
    records=cursor.fetchall()
    insertObject=[]
    columnNames= [column[0] for column in cursor.description]
    for record in records:
        insertObject.append( dict( zip( columnNames , record ) ) )
    
    cursor.close()
    return (json.dumps(insertObject))

@app.route('/searchcapacity/min<int:min>max<int:max>')
def searchCapacity(min,max):
    cursor=mysql.connection.cursor()
    cursor.execute(""" SELECT * FROM Homestay WHERE Homestay_capacity>='{0}' AND Homestay_capacity<='{1}' """.format(min,max))
    records=cursor.fetchall()
    insertObject=[]
    columnNames= [column[0] for column in cursor.description]
    for record in records:
        insertObject.append( dict( zip( columnNames , record ) ) )
    
    cursor.close()
    return (json.dumps(insertObject))


@app.route('/searchprice/min<int:min>max<int:max>')
def searchPrice(min,max):
    cursor=mysql.connection.cursor()
    cursor.execute(""" SELECT * FROM Homestay WHERE Homestay_price>='{0}' AND Homestay_price<='{1}' """.format(min,max))
    records=cursor.fetchall()
    insertObject=[]
    columnNames= [column[0] for column in cursor.description]
    for record in records:
        insertObject.append( dict( zip( columnNames , record ) ) )
    
    cursor.close()
    return (json.dumps(insertObject))