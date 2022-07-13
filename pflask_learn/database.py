import psycopg2
from tkinter import * 
import tkinter.messagebox
# database connection
class database_conn:
    try:
        conn = psycopg2.connect(dbname='application',
                                user='postgres',
                                password=2004,
                                host='localhost',
                                port=5432)
        print('[+]you are connected')
    except:
        print(" something went wrong ")
def connect_and_insert_or_update(query):
    connet = database_conn.conn
    curr = connet.cursor()
    try:
        print(query)
        curr.execute(query)
        print("data entered")
    except Exception as e:
        print('error :',e)
    connet.commit()
    connet.close()
def connect_and_show_data(query):
    connet = database_conn.conn
    curr = connet.cursor()
    curr.execute(query)
    milgaya = curr.fetchall()
    curr.close()
    return milgaya
# making function for button

def change_data():
    label_enter_app = Label(root,text=" enter app number :")
    label_enter_score = Label(root,text=" enter score number :")
    app_id = Entry(root)
    change_entry = Entry(root)
    def submm():
        try:
            query = "Update admission set score={0} where app_no={1}".format(app_id.get(),change_entry.get())
            connect_and_insert_or_update(query)
        except:
            tkinter.messagebox.showerror("error","something went wrong")
    subm = Button(root,text='submit',command=lambda:submm())
    change_entry.grid(row=1,column=1)
    app_id.grid(row=2,column=1)
    subm.grid(row=3,column=1)
    label_enter_app.grid(row=1,column=0)
    label_enter_score.grid(row=2,column=0)
    b1.destroy();b2.destroy();b3.destroy();label1.destroy()

def insert_data():
    heading = Label(root,text=" enter details:")
    label11 = Label(root,text='enter app_number :')
    label2 = Label(root,text='enter name :')
    label3 = Label(root,text='enter score :')
    ent1 = Entry(root);ent2 = Entry(root);ent3 = Entry(root)
    def insertin():
        try:
            queryss = '''INSERT INTO admission values('{0}','{1}','{2}','{3}')'''.format(ent1.get(),ent2.get(),ent3.get(),"verified") 
            print(queryss)
            connect_and_insert_or_update(queryss)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("error","somethign went wrong") 
    but1 = Button(root,text='submit',command=lambda:insertin())
    heading.grid(row=0,column=0)
    label11.grid(row=1,column=0)
    label2.grid(row=2,column=0)
    label3.grid(row=3,column=0)
    but1.grid(row=4,column=1)
    ent1.grid(row=1,column=1)
    ent2.grid(row=2,column=1)
    ent3.grid(row=3,column=1)
    b1.destroy();b2.destroy();b3.destroy();label1.destroy()

    # status will be set automatically
# making a tkinter gui
def show_data():
    label12 = Label(root,text="enter data to show data")
    labelapp_no = Label(root,text="enter application number :")
    entry12 = Entry(root)
    label12.grid(row=0,column=1)
    labelapp_no.grid(row=1,column=0)
    entry12.grid(row=1,column=1)
    def showshiz():
        try:
            query = "Select * from admission where app_no"+"="+"'{0}'".format(entry12.get())
            conconvar = connect_and_show_data(query)
            tkinter.messagebox.showinfo("your data","{0}".format(conconvar))
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("error","somethign went wrong")  
    but1 = Button(root,text='submit',command=lambda:showshiz())
    but1.grid(row=3,column=1)
    b1.destroy();b2.destroy();b3.destroy();label1.destroy()
root = Tk()
# widgets creation
label1 = Label(root,text=" select any option from below")
b1 = Button(root,text=' click me to change data',command=change_data)
b2 = Button(root,text=' click me to insert data',command=insert_data)
b3 = Button(root,text=' click me to show data',command=show_data)
label1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
root.mainloop()


