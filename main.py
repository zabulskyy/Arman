import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'flask-mail'))

from flask import Flask, request, flash
from smtplib import SMTPRecipientsRefused
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'some_secret'
# mail=Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'saint.arman.university@gmail.com'
app.config['MAIL_PASSWORD'] = 'armanthebest123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/computer-science')
def cs():
    return app.send_static_file('computer-science.html')


@app.route('/economics')
def ec():
    return app.send_static_file('economics.html')


@app.route('/apply')
def application_form():
    return app.send_static_file('application-form.html')


@app.route('/apply', methods=["POST"])
def send_mail():
    try:
        fn = request.form['fn']
        sn = request.form['sn']
        fac = request.form['fac']
        email = request.form['email']
        address = request.form['adr']
        phone = request.form['cp']
        phone2 = request.form['ap']
        gender = request.form['gender']
        par = request.form['parents_name']
        par_cont = request.form['parents_contacts']
        marks = request.form['marks']
        gy = request.form['grad_year']
        ai = request.form['ai']

        content1 = "Dear {0} {1}. \n" \
                   "We are happy to meet you at our Fictum University of Saint Arman. \n" \
                   "We greet you at {2} faculty and wish productive studying and unforgettable experience. \n" \
                   "See you on 1st September\n" \
                   "Your faithful, Arman\n" \
                   "P.S. we'll send you an information\n" \
                   "P.S.S wait for one more letter to check up correctness " \
                   "of information you've entered".format(fn, sn, fac)
        msg1 = Message("Greetings", sender='armankingofkings@gmail.com', recipients=[email])
        msg1.body = content1
        mail.send(msg1)

        content2 = "Dear {0} {1}.\n\n" \
                   "Here is the data you entered into our application form:\n\n" \
                   "Name: {0} {1}\n" \
                   "Gender: {6}\n" \
                   "Faculty: {2}\n" \
                   "Address: {3}\n" \
                   "Phone: {4}\n" \
                   "Additional phone: {5}\n" \
                   "Parents name: {7}\n" \
                   "Parents contacts: {8}\n" \
                   "School marks: {9}\n" \
                   "Graduation year: {10}\n" \
                   "Additional information: \n{11}\n" \
                   "Your faithful, Arman".format(fn, sn, fac, address, phone, phone2,
                                                 gender, par, par_cont, marks, gy, ai)
        msg2 = Message("Welcome", sender='armankingofkings@gmail.com', recipients=[email])
        msg2.body = content2
        mail.send(msg2)

        return app.send_static_file('application-form-access.html')
    except SMTPRecipientsRefused:
        flash("Incorrect email", "error")
        return app.send_static_file('application-form.html')


@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
