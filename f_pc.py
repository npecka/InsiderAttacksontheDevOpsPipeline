from flask import Flask, request, render_template
from producer import producer_create
from consumer import consumer_create
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('pc-setup-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    sslchoice = request.form['sslchoice']
    porc = request.form['porc']
    bserver = request.form['bserver']
    clientid = request.form['clientid']
    topic = request.form['topic']
    sprotocol = request.form['sprotocol']
    smechanism = request.form['smechanism']
    suser = request.form['suser']
    spass = request.form['spass']
    if porc == 'p':
        if sslchoice == 'yes':
            producer = producer_create(bserver, clientid, sprotocol, smechanism, suser, spass)

        else:
            producer = producer_create(bserver, clientid)
    else:
        if sslchoice == 'yes':
            consumer = consumer_create(topic, bserver, clientid, sprotocol, smechanism, suser, spass)
        else:
            consumer = consumer_create(topic, bserver, clientid)
