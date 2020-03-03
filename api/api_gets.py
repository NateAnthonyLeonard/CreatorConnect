from flask import request, redirect, flash
from api_main import app, mongo
from response import Response

#genas change
# Index
@app.route('/')
def index():
    return Response(200, {}).serialize()

@app.route('/userCount')
def userCount():
    totalUsers = mongo.db.users.count()
    return Response(200, totalUsers).serialize()
# /users

@app.route('/users')
def listUsers():
    # Search for first 10 users and typecast to list
    users = list(mongo.db.users.find({}).limit(10))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /users
@app.route('/users/page/<int:page>')
def listUsersPagination(page):
    # if less than 1
    if page < 1:
        return Response(400, {"error":"that's not gonna work"}).serialize()

    # Search for first 10 users and typecast to list
    users = list(mongo.db.users.find({}).skip((page-1)*9).limit(9))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /allUsers
@app.route('/allUsers')
def listAllUsers():
    # Search for all users and typecast to list
    # NOTE- this is specifically used to test CSS/JS features with the frontend team. 
    users = list(mongo.db.users.find({}))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /randUsers
@app.route('/allRandUsers')
def listRandomUsers():
    # Search for random users and typecast to list
    numUsers = mongo.db.users.count()
    users = list(mongo.db.users.aggregate([ { "$sample": { "size": numUsers } } ]))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /users/<count>
@app.route('/users/<int:count>')
def listUserCount(count):
    users = list(mongo.db.users.find({}).limit(count))
    return Response(200, users).serialize()

# /getUser/<username>
@app.route('/getUser/<string:username>')
def searchByUsername(username):
    # Returns user specified object
    users = list(mongo.db.users.find({"fsu_id" : username}))

    return Response(200, users).serialize()

# /getByGradDate/<year>
@app.route('/getByGradDate/<int:year>')
def listByGradDate(year):
    # Returns array of 3 users with specified grad date
    users = list(mongo.db.users.find({"grad_date" : year}).limit(3))
    return Response(200, users).serialize()

# /getByGradDate/<year>/<count>
@app.route('/getByGradDate/<int:year>/<int:count>')
def chooseCountGradDate(year, count):
    # Returns array of specified amount of users with specified grad date
    users = list(mongo.db.users.find({"grad_date" : year}).limit(count))
    return Response(200, users).serialize()

@app.route('/projectsRand')
def proyectos():
    numProj = mongo.db.projects.count()
    projectLst = list(mongo.db.projects.aggregate([ { "$sample": { "size": numProj } } ]))

    # Return new response object formatted with users
    return Response(200, projectLst).serialize()

#search by project name

@app.route('/getProjects/<string:projName>')
def searchProjByProjname(projName):
    # Returns user specified object
    project = list(mongo.db.projects.find({"projTitle" : projName}))

    return Response(200, project).serialize()
# ideas
# /getByGradRange
# /getBySkills