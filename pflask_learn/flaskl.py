from flask import Flask, render_template, request
import psycopg2

#connecting and handling databases
class database_connection:
    class try_connet:
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
    class do_something(try_connet):
            def insert_data(query):
                conn = psycopg2.connect(dbname='application',
                                    user='postgres',
                                    password='2004',
                                    host="127.0.0.1",
                                    port='5432'
                                    )
                curr = conn.cursor()
                curr.execute(query)
                conn.commit()
                conn.close()
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


app.run('127.0.0.1','5050',debug=True)
