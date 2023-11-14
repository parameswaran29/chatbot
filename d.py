import re
import speech_recognition as sr
import pyttsx3
from difflib import SequenceMatcher
from werkzeug.utils import secure_filename
from gtts import gTTS
import os


import ar_master
from flask import Flask, render_template, flash, request, session, current_app, send_from_directory

app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
mm = ar_master.master_flask_code()

@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/admin_log", methods=['GET', 'POST'])
def admin_log():
    error = None
    if request.method == 'POST':
        un = request.form['uname']
        pa = request.form['pass']

        pa = pa.strip()
        un = un.strip()
        if un == "admin" and pa == "admin":
            return render_template('admin_home.html', error=error)
        else:
            return render_template('admin_log.html', error=error)
    return render_template("admin_log.html")

@app.route("/student_log", methods=['GET', 'POST'])
def student_log():
    error = None
    if request.method == 'POST':

        un = request.form['uname']
        pa = request.form['pass']
        qry = "SELECT * from student_details where username='" + str(un) + "' and password='" + str(pa) + "'"
        result = mm.select_login(qry)
        if result == "no":
            return render_template('student_log.html', flash_message=True, data="Login Failed")
        else:
            session['student'] = request.form['uname']
            return render_template('student_home.html')
    return render_template('student_log.html')

@app.route("/parent_log", methods=['GET', 'POST'] )
def parent_log():
    if request.method == 'POST':

        un = request.form['uname']
        pa = request.form['pass']
        qry = "SELECT * from parent_details where username='" + str(un) + "' and password='" + str(pa) + "'"
        result = mm.select_login(qry)
        if result == "no":
            return render_template('parent_log.html', flash_message=True, data="Login Failed")
        else:
            session['parent'] = un
            return render_template('parent_home.html')
    return render_template('parent_log.html')


@app.route("/admin_home")
def admin_home():

    return render_template('admin_home.html')

@app.route("/student_reg", methods=['GET', 'POST'])
def student_reg():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        dob = request.form['dob']
        address = request.form['address']
        gender = request.form['gender']
        email = request.form['email']
        department = request.form['department']
        year = request.form['year']
        semester = request.form['semester']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("student_details")
        qry = ("insert into student_details values('" + str(maxin) + "','" + str(name) + "','" + str(
            contact) + "','" + str(dob) + "','" + str(address) + "','" + str(gender) + "','" + str(
            email) + "','" + str(
            department) + "','" + str(year) + "','" + str(semester) + "','" + str(
            username) + "','" + str(password) + "')")
        result = mm.insert_query(qry)

        return render_template('student_log.html')
    return render_template('student_reg.html')

@app.route("/parent_reg", methods=['GET', 'POST'])
def parent_reg():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        address = request.form['address']
        gender = request.form['gender']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        nos = request.form['nos']

        maxin = mm.find_max_id("parent_details")
        qry = ("insert into parent_details values('" + str(maxin) + "','" + str(name) + "','" + str(
            contact) + "','" + str(address) + "','" + str(gender) + "','" + str(email) + "','" + str(
            username) + "','" + str(
            password) + "','" + str(
            nos) + "')")
        result = mm.insert_query(qry)

        return render_template('parent_log.html')
    return render_template('parent_reg.html')

@app.route("/add_trained_set", methods=['GET', 'POST'])
def add_trained_set():
    if request.method == 'POST':
        query = request.form['query']
        query = query.lower()

        response = request.form['response']
        f = request.files['file']
        try:
            f.save(os.path.join("static/uploads/",secure_filename(f.filename)))
            maxin = mm.find_max_id("trained_set")
            qry = ("insert into trained_set values('" + str(maxin) + "','" + str(query) + "','" + str(
                response) + "','" + str(f.filename) + "','')")
            result = mm.insert_query(qry)
            return render_template('add_trained_set.html')
        except:
          maxin = mm.find_max_id("trained_set")
          qry = ("insert into trained_set values('" + str(maxin) + "','" + str(query) + "','" + str(
            response) + "','no_image.jpg','','')")
          result = mm.insert_query(qry)
          return render_template('add_trained_set.html')

    return render_template('add_trained_set.html')

@app.route("/student_details")
def student_details():
    data=mm.select_direct_query("select name,contact,dob,address,gender,email,department,year,semester from student_details")

    return render_template('student_details.html',items=data)

@app.route("/parent_details")
def parent_details():
    data=mm.select_direct_query("select name,contact,address,gender,email,nos from parent_details")

    return render_template('parent_details.html',items=data)

@app.route("/student_home")
def student_home():


    return render_template('student_home.html')

@app.route("/student_query", methods=['GET', 'POST'])
def student_query():
    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        a = engine.runAndWait()

    if request.method == 'GET':
        return render_template('student_query.html')
    elif request.method == 'POST':
        try:
            if request.form['Ask'] == 'Ask':
                query = request.form['p']
                query = query.lower()
                qry = "SELECT id,query,response,graphical from trained_set"
                data = mm.select_direct_query(qry)
                res2=''
                res3=''
                dd=0
                for row in data:
                    que = row[1]
                    v = SequenceMatcher(None, que, query).ratio()
                    ########
                    print(v)
                    if dd<v:
                        dd=v
                        res2=row[2]
                        res3=row[3]
                    ########
                    # ved = "update trained_set set percen='" + str(v) + "' where id='" + str(id) + "'"
                    # mm.insert_query(ved)


            # qry = "SELECT response,graphical from trained_set where percen='1'"
            # xa1 = mm.select_direct_query(qry)
            #
            # xa = xa1[0][0]
            # bv = xa1[0][1]

            xa=res2
            bv=res3


            #
            v = "True"
            if (bv == "no_image.jpg"):
                v = "false"
            #     bv = "no_image.jpg"



            query = request.form['p']
            a = session['student']
            maxin = mm.find_max_id("query_details")
            qry = ("insert into query_details values('" + str(maxin) + "','" + str(query) + "','" + str(
                xa) + "','" + str(bv) + "','Student','" + str(a) + "')")
            result = mm.insert_query(qry)
            if (xa != ''):
                SpeakText(xa)
                session['xa'] = xa
            return render_template('student_query.html', nm=xa, image=bv, flashMessage=v)
        except:
            return render_template('student_query.html')
    return render_template('student_query.html')


@app.route("/query_s_details")
def query_s_details():
    c=session['student']
    print(c)
    data=mm.select_direct_query("select query,answer,image from query_details where username='"+ str(c) +"'")

    return render_template('query_s_details.html',items=data)

@app.route("/parent_query", methods=['GET', 'POST'])
def parent_query():
    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        a = engine.runAndWait()

    if request.method == 'GET':
        return render_template('parent_query.html')
    elif request.method == 'POST':
        try:
            if request.form['Ask'] == 'Ask':
                query = request.form['p']
                query = query.lower()
                qry = "SELECT id,query,response,graphical from trained_set"
                data = mm.select_direct_query(qry)
                res2 = ''
                res3 = ''
                dd = 0
                for row in data:
                    que = row[1]
                    v = SequenceMatcher(None, que, query).ratio()
                    ########
                    print(v)
                    if dd < v:
                        dd = v
                        res2 = row[2]
                        res3 = row[3]
                    ########
                    # ved = "update trained_set set percen='" + str(v) + "' where id='" + str(id) + "'"
                    # mm.insert_query(ved)

            # qry = "SELECT response,graphical from trained_set where percen='1'"
            # xa1 = mm.select_direct_query(qry)
            #
            # xa = xa1[0][0]
            # bv = xa1[0][1]

            xa = res2
            bv = res3
            print(bv)
            #
            v = "True"
            if (bv == "no_image.jpg"):
                v = "false"
            #     bv = "no_image.jpg"

            query = request.form['p']
            a = session['parent']
            maxin = mm.find_max_id("query_details")
            qry = ("insert into query_details values('" + str(maxin) + "','" + str(query) + "','" + str(
                xa) + "','" + str(bv) + "','Parent','" + str(a) + "')")
            result = mm.insert_query(qry)
            if (xa != ''):
                SpeakText(xa)
                session['xa'] = xa
            return render_template('parent_query.html', nm=xa, image=bv, flashMessage=v)
        except:
            return render_template('parent_query.html')
    return render_template('parent_query.html')




@app.route("/query_p_details")
def query_p_details():
    c=session['parent']
    print(c)
    data=mm.select_direct_query("select query,answer,image from query_details where username='"+ str(c) +"'")

    return render_template('query_p_details.html',items=data)
@app.route("/parent_home")
def parent_home():
    return render_template('parent_home.html')


@app.route("/query_a_details")
def query_a_details():

    data=mm.select_direct_query("select query,answer,image,user,username from query_details")

    return render_template('query_a_details.html',items=data)

@app.route("/speech")
def speech():
    xa=session['xa']


    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        a = engine.runAndWait()

    SpeakText(xa)
    v="false"
    return render_template('parent_query.html',nm=xa,flashMessage=v)


######################################
if __name__ == '__main__':
    app.debug = True
    app.run()