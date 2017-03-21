from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from smtplib import SMTPRecipientsRefused

from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'some_secret'
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'armankingofkings@gmail.com'
app.config['MAIL_PASSWORD'] = 'armantheking'
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

@app.route('/apply', methods = ["POST"])
def send_mail():
    try:
        fn = request.form['fn']
        sn = request.form['sn']
        fac = request.form['fac']
        email = request.form['email']
        content = "Hello, {0} {1}. \n" \
                  "We are happy to meet you at our Fictum University of Saint Arman. \n" \
                  "We greet you at {2} faculty and wish productive studying and unforgettable experience. \n" \
                  "See you on 1st September\n" \
                  "Your faithful, Arman".format(fn, sn, fac)
        msg = Message("Welcome", sender='armankingofkings@gmail.com',recipients = [email])
        msg.body = content
        mail.send(msg)
        return app.send_static_file('application-form.html')
    except SMTPRecipientsRefused:
        flash("Incorrect email", "error")
        return app.send_static_file('application-form.html')



@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
