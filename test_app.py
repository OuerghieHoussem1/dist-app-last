from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

import pymongo
from bson.objectid import ObjectId


import time

import RPi.GPIO as GPIO

import pigpio


PIGPIO  = pigpio.pi()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_SAVEUR_1 = 4
PIN_SAVEUR_2 = 17
PIN_SAVEUR_3 = 22
PIN_SAVEUR_4 = 23
PIN_SAVEUR_5 = 9
PIN_EAU = 8




GPIO.setup(PIN_SAVEUR_1, GPIO.OUT)
GPIO.setup(PIN_SAVEUR_2, GPIO.OUT)
GPIO.setup(PIN_SAVEUR_3, GPIO.OUT)
GPIO.setup(PIN_SAVEUR_4, GPIO.OUT)
GPIO.setup(PIN_SAVEUR_5, GPIO.OUT)
GPIO.setup(PIN_EAU, GPIO.OUT)

app = Flask(__name__)
socketio = SocketIO(app)


client = pymongo.MongoClient("mongodb+srv://houssemouerghie:testtest@cluster0.cmk7sds.mongodb.net/")


db = client["app-test"] #To change based on the machine


cards = db["cards"]
drinks = db["drinks"]
users = db["drinks"]



#Routes code

#-------------------WEB PAGES-------------------#


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/passCard')
def passCard():
    return render_template('./passCard.html')

@app.route('/chooseTaste')
def chooseTaste():
    return render_template('./chooseTaste.html')

@app.route('/chooseIntensity')
def chooseIntensity():
    return render_template('./chooseIntensity.html')

@app.route('/success')
def success():
    return render_template('./success.html')


#-------------------DRINKS MANAGEMENT-------------------#


@app.route('/drinks')
def getdrinks():
    drinks_list = []
    for drink in drinks.find():
        drinks_list.append({
            '_id': str(drink['_id'])
        })
    return jsonify(drinks_list)

@app.route('/drinks', methods=['POST'])
def addDrink():
    data = request.get_json()
    new_drink = {
        'name': data['name'],
        'type': data['type']
    }
    drink_id = drinks.insert_one(new_drink).inserted_id
    return {'message': 'Drink added successfully', 'drink_id': str(drink_id)}

@app.route('/drinks/<drink_id>', methods=['PUT'])
def updateDrink(drink_id):
    data = request.get_json()
    drinks.update_one({'_id': ObjectId(drink_id)}, {'$set': data})
    return {'message': f'Drink {drink_id} updated successfully'}

@app.route('/drinks/<drink_id>', methods=['DELETE'])
def deleteDrink(drink_id):
    drinks.delete_one({'_id': ObjectId(drink_id)})
    return {'message': f'Drink {drink_id} deleted successfully'}


#-------------------CARDS MANAGEMENT-------------------#


@app.route('/cards')
def getCards():
    cards_list = []
    for card in cards.find():
        cards_list.append({
            '_id': str(card['_id']),
            'number': card['number'],
            'balance': card['balance']
        })
    return jsonify(cards_list)

@app.route('/checkCards', methods=['POST'])
def addCard():
    data = request.get_json()
    new_card = {
        'number': data['number'],
        'balance': data['balance']
    }
    card_id = cards.insert_one(new_card).inserted_id
    return {'message': 'Card added successfully', 'card_id': str(card_id)}

""" @app.route('/cards', methods=['POST'])
def addCard():
    data = request.get_json()
    # Process the data from the POST request
    return {'message': 'POST request 1 successful'} """

@app.route('/cards/<card_id>', methods=['PUT'])
def updateCard(card_id):
    data = request.get_json()
    cards.update_one({'_id': ObjectId(card_id)}, {'$set': data})
    return {'message': f'Card {card_id} updated successfully'}

@app.route('/cards/<card_id>', methods=['DELETE'])
def deleteCard(card_id):
    cards.delete_one({'_id': ObjectId(card_id)})
    return {'message': f'Card {card_id} deleted successfully'}


#-------------------USER MANAGEMENT-------------------#


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = {
        'username': data['username'],
        'password': data['password']
    }
    user_id = users.insert_one(new_user).inserted_id
    return {'message': 'User signup successful', 'user_id': str(user_id)}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({'username': data['username'], 'password': data['password']})
    if user:
        return {'message': 'User login successful'}
    else:
        return {'message': 'User login failed'}
    


#-------------------Pump controls-------------------#
@app.route("/taste/<taste>/<intensity>")
def taste(taste, intensity):

    print(taste)   
    print(intensity)   
    print("Started")

    taste = int(taste)
    intensity = int(intensity)

    taste = int(taste)
    intensity = int(intensity)
    if(taste==0):
        GPIO.output(PIN_SAVEUR_1, GPIO.HIGH)
    if(taste==2):
        GPIO.output(PIN_SAVEUR_2, GPIO.HIGH)
    if(taste==3):
        GPIO.output(PIN_SAVEUR_3, GPIO.HIGH)
    if(taste==4):
        GPIO.output(PIN_SAVEUR_4, GPIO.HIGH)
    if(taste==5):
        GPIO.output(PIN_SAVEUR_5, GPIO.HIGH)
    if(taste==6):
        GPIO.output(PIN_EAU , GPIO.HIGH)

    time.sleep(intensity/1000)

    if(taste==0):
        GPIO.output(PIN_SAVEUR_1, GPIO.LOW)
    if(taste==2):
        GPIO.output(PIN_SAVEUR_2, GPIO.LOW)
    if(taste==3):
        GPIO.output(PIN_SAVEUR_3, GPIO.LOW)
    if(taste==4):
        GPIO.output(PIN_SAVEUR_4, GPIO.LOW)
    if(taste==5):
        GPIO.output(PIN_SAVEUR_5, GPIO.LOW)
    if(taste==6):
        GPIO.output(PIN_EAU , GPIO.LOW)

    
    GPIO.output(PIN_EAU , GPIO.HIGH)
    time.sleep(4)
    GPIO.output(PIN_EAU , GPIO.LOW)

    print("Finished")
    return {'message': 'Good'}

#Socket code
@socketio.on('connect')
def handle_connect():
    print('WebSocket connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('WebSocket disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)  # Change the port as needed