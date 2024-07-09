from flask import Flask, request, jsonify
import json

app = Flask(__name__)

fridge = {'apple', 'pear'}  

@app.route('/')
def index():
    return('Welcome to the Fridge')

@app.route('/display', methods = ['GET'])
def openFridge():
    if fridge == {}:
        return jsonify({"Response" : "Fridge is empty"})
    return jsonify({'Response' : str(fridge)})

@app.route('/get', methods = ['GET'])
def checkFridge():
    if fridge == {}:
        return jsonify({"Response" : "Fridge is empty"})
    food = request.args.get('item')
    if food in fridge:
        return jsonify({'Response' : 'Your food is in the fridge'})
    return jsonify({'Response' : 'Sorry, your food is not in the fridge'})

@app.route('/insert', methods = ['PUT'])
def putInFridge():
    item = request.args.get('item')
    fridge.add(item)
    return jsonify({"response" : "food successfully added"})

@app.route('/remove', methods = ['DELETE'])
def takeFromFridge():
    item = request.args.get('item')
    if item not in fridge:
        return jsonify({"response" : "Could not find the item in the fridge!"})
    fridge.remove(item)
    return jsonify({"reponse" : "item removed successfully!"})

if __name__ == '__main__':
    app.run(debug = True)