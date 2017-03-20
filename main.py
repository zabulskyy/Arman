from flask import Flask

app = Flask(__name__)


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


@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
