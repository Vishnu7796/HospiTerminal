from flask import Flask,render_template,flash,request,redirect,session,url_for
from Database import DBHelper, tempHelper
from Login import LoginDoctor, LoginHelper
import speech_recognition as sr


# Use frepik for good quality images
# add date of birth to signup and accordingly database
# taking database online
# doctor portal designing
# updating information
# table for each separate patient and doctor
# adding role in login
# use value to directly fill the data in input from the backend
# advice and diagnosis are interchangeable

cur = LoginHelper()
act = DBHelper()
doc = LoginDoctor()
temp = tempHelper()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gjfgs;dfjgds'



@app.route("/mail/<name>,<age>,<email>,<symptoms>,<prescription>,<advice>")
def mail(name,age,email,symptoms,prescription,advice):

    from send_mail import sendMail

    sendMail(name,age,email,symptoms,prescription,advice)

    return redirect(url_for('Doctor_Portal',Para2='Prescription',Para1 = 'Diagnosis'))



@app.route('/takecommand/')
def takecommand():
    r = sr.Recognizer()
    Advice = "Advice"
    Prescription = "Prescription"

    while (True):

        with sr.Microphone() as source:                                                             

            print("Listening.....")
            # flash("Listening to Advice.....",category="success")
            audio = r.listen(source)
            
            try:
                print("Recognising....")
                # flash("Recognizing....")
                Advice = r.recognize_google(audio , language = "en-in")

                print("You Said: ",format(Advice))
                break
            except:
                print("Sorry Could you repeat")
                # flash("Sorry! could you repeat",category='error')
    
    while(True):  

        with sr.Microphone() as source:                                                               

            print("Listening.....")
            audio = r.listen(source)
            
            try:
                print("Recognising....")
                Prescription = r.recognize_google(audio , language = "en-in")

                print("You Said: ",format(Prescription))
                break
            except:
                print("Sorry Could you repeat")

    return redirect(url_for('Doctor_Portal',Para2 = Prescription,Para1 = Advice))



@app.route("/doctor_portal/<Para1>,<Para2>",methods=['POST','GET'])
def Doctor_Portal(Para1,Para2 ):

    row = temp.fetch_user(session['emailId'])
    print(row)

    if row:
        session['Pat_name'] = row[0][2]
        session['Pat_email'] = row[0][0]
        session['Pat_symptoms'] = row[0][3]
        session['Pat_age'] = 18
        records = act.fetch_user(session['Pat_email'])

    else:
        flash("No patient available. Visit after some time")
        return redirect(url_for('Logout'))

    if request.method == 'POST':

        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        symptoms = request.form.get('symptoms')
        prescription = request.form.get('prescription')
        advice = request.form.get('advice')

        temp.delete_user(session['Pat_email'])

        session.pop('Pat_name',None)
        session.pop('Pat_email',None)
        session.pop('Pat_symptoms',None)
        session.pop('Pat_age',None)

        act.insert_user(email,advice,symptoms,prescription)

        return redirect(url_for('mail',name=name,age=age,email=email,symptoms=symptoms,prescription=prescription,advice=advice))

    return render_template("Doc_Port.html",title ="Doc_Portal",Advice = Para1, Prescription = Para2, records = records)


@app.route("/")
def Home():
    return render_template("Home.html", title = "Home", Home="active")


@app.route("/book_appointment/",methods =['POST','GET'])
def Book():
    if request.method == 'POST':

        name = request.form.get('name')
        if name == '':
            name = session['firstName']

        age = request.form.get('age')

        email = request.form.get('email')
        if email == '':
            email = session['emailId']

        symptoms = request.form.get('symptoms')
        # phone = request.form.get('phone')
        # male = request.form.get('male')
        # female = request.form.get('female')
        doctor = request.form.get('doctor')

        if doctor == '':
            doctor = 'default'

        temp.insert_user(email,name,symptoms,doctor)

        flash("Appointment Done! Thank you")
        return redirect('/logout/')

    return render_template("Book.html",title = "Appointment")



@app.route("/about_us/")
def About_Us():
    try:
        if(session['loggedin'] != True):
            return redirect('/login/')
    except:
            return redirect('/login')
        
    return render_template("About_Us.html",title = "About",About = "active")



@app.route("/login/",methods=['POST','GET'])
def Login(): 

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        is_doctor = request.form.get('doctor')

        # print(is_doctor)
        # print(email)
        # print(password)

        row = []

        if is_doctor:
            row = doc.fetch_user(email)
            # print('doc')
        else:
            row = cur.fetch_user(email)
            # print('cur')

        if email == '':
            return render_template("Login.html",title = "Login")

        if row == None:
            flash('Please SignIn, Account not found',category = 'error')
            return redirect('/signup/')

        elif row[2] != password:
            flash('Incorrect Password!',category = 'error')

        else:
            # flash('Logged In',category = 'success')
            session['loggedin'] = True
            session['emailId'] = email
            session['firstName'] = row[1]
            session['is_doctor'] = False

            if is_doctor:
                session['is_doctor'] = True
                # print('yep')

            # print(session['is_doctor'])
            return redirect('/')
        
    return render_template("Login.html",title = "Login")



@app.route("/signup/",methods=['POST','GET'])
def Sign_Up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        is_doctor = request.form.get('doctor')

        print(is_doctor)

        if len(email) < 4:
            flash('Email Invalid',category='error')

        elif cur.fetch_user(email) != None:
            flash('Email already exists', category='error')

        elif doc.fetch_user(email) != None:
            flash('Email already exists',category ='error')

        elif len(firstName) < 2:
            flash('Invalid Name',category='error')

        elif len(password1) < 4:
            flash('Password too short',category = 'error')

        elif password1 != password2:
            flash('Passwords don\'t match',category = 'error')

        else:
            if is_doctor:
                doc.insert_user(email,firstName,password1)
                # print('doc')
            else:
                cur.insert_user(email,firstName,password1)
                # print('cur')

            flash('Account created successfully',category='success')

            return redirect('/login/')

    return render_template("Sign_Up.html",title = "Sign_Up")


@app.route("/logout/")
def Logout():
    
    if(session['loggedin'] != True):
        return redirect('/login/')

    session.pop('loggedin',None)
    session.pop('emailId',None)
    session.pop('firstName',None)
    flash("Logged Out Successfully",category = 'success')
    return redirect ('/login/')


if __name__ == "__main__":
    app.run(debug = True)
    