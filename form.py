from flask import Flask, render_template, request
import smtplib

@app.route('/submit_form', methods=['POST'])
def submit_form(): #name of the url on js
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']

        user = "email"
        password = "password"
        message = str(name) + '\n\n' + str(email) + '\n\n' + str(msg)
        server = smtplib.SMTP("smtp.gmail.com:587") #remember allow less secure app access on gmail
        server.starttls()
        server.login(user, password)
        server.sendmail(user, user, message) #from, to, message
        server.quit()

        return render_template('thankyou.html') #or return ('', 204) if showing a message through js
