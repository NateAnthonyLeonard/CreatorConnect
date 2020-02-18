from flask import request, redirect, flash, session, url_for, make_response
from api_main import app, mongo
from response import Response
import bcrypt
import json
from flask.sessions import SecureCookieSessionInterface
import time
from bson.objectid import ObjectId

app.secret_key = 'mysecret' 

#global booleans that will keep track of errors
wrongPassword = False 
nonexistentUser = False
existentUser = False
person = ""

@app.route('/register', methods=['POST'])
def createNewUser():
    global wrongPassword 
    global nonexistentUser
    global existentUser
    global person
    document = request.form.to_dict()
    name = document['firstName'] + ' ' + document['lastName']
    emailEntered = document['fsuEmail'].lower()
    # TODO: Add verification for fsu.edu email // also email existence module 

    #search to see if a user with this email already exists
    user = mongo.db.users.find_one({'email': emailEntered})

    rawPassword = document['password']
    rawPassword.encode('utf-8')
    hashedPassword = bcrypt.hashpw(rawPassword.encode('utf8'), bcrypt.gensalt())
    skillsArray = [document['firstSkill'], document['secondSkill'], document['thirdSkill'], document['fourthSkill'], document['fifthSkill']]

    #based on the response send through, booleans explain the routes
    if user is None:
        wrongPassword = False
        nonexistentUser = False
        existentUser = False
        mongo.db.users.insert_one({'name': name, 'email': document['fsuEmail'].lower(), 'hashedPassword': hashedPassword, 'gradYear': document['gradYear'], 'skills': skillsArray})
        user = mongo.db.users.find_one({'email': emailEntered})
        session['username'] = user['name']
        person = user['_id']
        return redirect("http://localhost:3000/cards")
    else:
        wrongPassword = False
        nonexistentUser = False
        existentUser = True
        return redirect("http://localhost:3000/cards")

@app.route('/login', methods=['POST', 'GET'])
def login(): 
  global wrongPassword 
  global nonexistentUser
  global existentUser
  global person
  if request.method == 'POST': 
    document = request.form.to_dict()
    emailEntered = document['fsuEmail'].lower()
    passwordEntered = document['password']
    
    #search for email in DB
    user = mongo.db.users.find_one({'email': emailEntered})

    #based on the response send through, booleans explain the routes
    if user is None:
        wrongPassword = False
        nonexistentUser = True
        existentUser = False
        return redirect("http://localhost:3000/cards")
    else:
        if (bcrypt.checkpw(passwordEntered.encode('utf8'), user['hashedPassword'])):
            wrongPassword = False
            nonexistentUser = False
            existentUser = False
            session['username'] = user['name'] #signs user in
            person = user['_id']
            return redirect("http://localhost:3000/cards")
        else:
            wrongPassword = True
            nonexistentUser = False
            existentUser = False
            return redirect("http://localhost:3000/cards")
  elif request.method == 'GET':
    if 'username' in session:
      return "0"

    else:
      if wrongPassword is True:
        wrongPassword = False
        nonexistentUser = False
        existentUser = False
        return "2"
      elif nonexistentUser is True:
        wrongPassword = False
        nonexistentUser = False
        existentUser = False
        return "3"
      elif existentUser is True:
        wrongPassword = False
        nonexistentUser = False
        existentUser = False
        return "1"

      else:
        wrongPassword = False
        nonexistentUser = False
        existentUser = False
        return "5"

#endponint to log user out using session.pop
@app.route('/logout', methods=['POST'])
def logout():
  session.pop('username')
  return redirect("http://localhost:3000/")

#experimental endpoint to avoid sending logged in users to the launch page
@app.route('/isLoggedIn', methods=['GET'])
def isLoggedIn():
  if 'username' in session:
    return "0"
  return "1"

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
  global person
  if request.method == 'GET':
    return "we will delete " + person
  elif request.method == 'POST': 
    session.pop('username')
    mongo.db.users.delete_one({'_id': person}) 
    return redirect("http://localhost:3000/")

