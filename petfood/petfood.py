from crypt import methods
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template

app = Flask('petfood')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

#GPIO.output(2, GPIO.LOW)
#time.sleep(4)
#GPIO.output(2, GPIO.HIGH)

@app.route('/')
def index():
    print('index')
    return render_template('index.html')

@app.route('/liga', methods=['GET'])
def liga():
    print('liga')
    GPIO.output(2, GPIO.LOW)
    return index()

@app.route('/desliga', methods=['GET'])
def desliga():
    print('desliga')
    GPIO.output(2, GPIO.HIGH)
    return index()


#app.run(host='172.21.28.16', debug=False)
app.run(host='127.0.0.1', debug=False)

