from types import new_class
from flask import Flask, render_template, request
import psycopg2

#connecting and handling databases
class database_connection:
    class try_connet:
        conn = psycopg2.connect(dbname='application',
                            user='postgres',
                            password='2004',
                            host="127.0.0.1",
                            port='5432'
                            )
        def testing():
            try:
                conn = psycopg2.connect(dbname='application',
                                    user='postgres',
                                    password='2004',
                                    host="127.0.0.1",
                                    port='5432'
                                    )
                return 1 
            except:
                return 0
    class do_something():
            def insert_data(query):
                connet = database_connection.try_connet.conn
                curr = connet.cursor()
                curr.execute(query)
                connet.commit()
                #connet.close()
            def fetch_data(vari):
                connet = database_connection.try_connet.conn
                curr = connet.cursor()
                query = "Select * from admission where app_no='{0}'".format(vari)
                curr.execute(query)
                gotdata = curr.fetchall()
                connet.commit()
                #connet.close()
                return gotdata
            def change_data(app_no,what,newdata):
                query = ''' Update admission set {0}='{1}' where app_no='{2}'; '''.format(what,newdata,app_no)
                connet = database_connection.try_connet.conn
                curr = connet.cursor()
                curr.execute(query)
                connet.commit()
#handling web app 
app = Flask(__name__)
isActive = database_connection.try_connet.testing()
print(isActive)
#main function
@app.route('/')
def route_user():
    global isActive
    global books
    books = [{'name':'book1','author':'author1','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
             {'name':'book2','author':'author2','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
             {'name':'book3','author':'author3','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'}]
    return render_template('index.html',username='guest',isActive=isActive,books=books)

#not main functions
@app.route('/<username>')
def function1(username): 
    global isActive
    isActive = '1'
    five = 6
    return render_template('index.html',username=username,
        isActive=isActive,
        five=five
    )

@app.route('/ano')
def rederanother():
    books = [{'name':'book1','author':'author1','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
            {'name':'book2','author':'author2','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
            {'name':'book3','author':'author3','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'}]
    return render_template('another.html',username='guest',isActive=isActive,books=books)

@app.route('/submitbook',methods=['POST'])
def submit_book():
    name = request.form['name']
    app_name = request.form['app_name']
    score = request.form['score']
    verified = 'verified'
    query = "Insert into admission values('{0}','{1}','{2}','{3}');".format(app_name,name,score,verified)
    isubm_query = database_connection.do_something.insert_data(query)
    return 'book name is {0} and author is {1}'.format(name,app_name)

@app.route('/find')
def find_page():
    return render_template('finddata.html')

@app.route('/finddata',methods=['POST'])
def lets_find():
    var1 = request.form['app_no']
    weget = database_connection.do_something.fetch_data(var1)
    listli = ['appliocation number :','name :','score :','verification status :']
    wegetlen = len(weget)
    return render_template('finded.html',weget=weget,listli=listli,wegetlen=wegetlen)

@app.route('/change')
def enter_data_to_change():
    return render_template('changedata.html')

@app.route('/changed',methods=['POST'])
def change_data():
    app_no = request.form['app_no']
    what = request.form['what']
    new_data = request.form['newdata']
    change_data = database_connection.do_something.change_data(app_no,what,new_data)
    return "<h1 align='center'> Data Updated</h1>"
app.run('127.0.0.1','5050',debug=True)
