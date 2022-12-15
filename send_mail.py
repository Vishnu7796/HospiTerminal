from email.message import EmailMessage
import smtplib

host_name = 'animelove26837@gmail.com'
password = 'uilkbgbbblhigpor'

def sendMail(name,age,email,symptoms,prescription,diagnosis):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp.login(host_name,password)

    print("login successfull")

    msg = EmailMessage()
    msg['Subject'] = "Prescription"
    msg['From'] = host_name 
    msg['To'] = email

    temp = '''
        background-color: white;
        color: black;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serifs;
        /* float: left; */
        overflow: hidden;
        padding: 10%;
    '''

    msg.set_content('Your Prescription is here!')

    msg.add_alternative(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctors Prescription</title>
    <style>
        #myData{temp}
   
    </style>
</head>
<body>
   
    <header id="myData">
        <img src="https://www.bing.com/th?id=OIP.D2RhOusLpRffjcXcTVfxYQHaE8&w=306&h=204&c=8&rs=1&qlt=90&o=6&dpr=1.15&pid=3.1&rm=2" alt="Wait" >

        <h1>Name        :{name}
          <br>
           Age         :{age}
          <br>
           Symptons    :{symptoms}
          <br>
           Prescription:{prescription}
          <br>
           Diagnosis   :{diagnosis}
          <br>
        </h1>

        <img src="https://th.bing.com/th/id/R.b691a0ef2a828f0bf778d5808e9bd3a9?rik=Mppgb0FAIs3THA&riu=http%3a%2f%2fdanipronails.com%2fwp-content%2fuploads%2fdrevanssignature.jpg&ehk=tvoulX3HhDknlgFN%2ffKwstIFfggctS9JfdN0ZIeWeJg%3d&risl=&pid=ImgRaw&r=0" alt="Wait" width="20%" >
     </header>      
    
</body>
</html>

    ''',subtype='html')
    smtp.send_message(msg)

    print("Email send successfully")