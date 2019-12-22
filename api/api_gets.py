from api.api_main import api_route, db
from api.response import Response

# Index
@api_route.route('/')
def index():
    return Response(200, {}).serialize()

# /users
@api_route.route('/users')
def listUsers():
    # Search for first 10 users and typecast to list
    users = list(db.users.find({}).limit(10))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /allUsers
@api_route.route('/allUsers')
@api_route.route('/allUsers/')
def api_listAllUsers():
    # Search for all users and typecast to list
    # NOTE- this is specifically used to test CSS/JS features with the frontend team. 
    users = list(db.users.find({}))

    # Return new response object formatted with users
    return Response(200, users).serialize()


# /users/<count>
@api_route.route('/users/<int:count>')
def listUserCount(count):
    users = list(db.users.find({}).limit(count))
    return Response(200, users).serialize()

# /randUsers
@api_route.route('/randUsers')
def listRandomUsers():
    # Search for random 5 users and typecast to list
    users = list(db.users.aggregate([ { "$sample": { "size": 5 } } ]))

    # Return new response object formatted with users
    return Response(200, users).serialize()

# /getUser/<username>
@api_route.route('/getUser/<string:username>')
def searchByUsername(username):
    # Returns user specified object
    users = list(db.users.find({"fsu_id" : username}))

    return Response(200, users).serialize()

# /getByGradDate/<year>
@api_route.route('/getByGradDate/<int:year>')
def listByGradDate(year):
    # Returns array of 3 users with specified grad date
    users = list(db.users.find({"grad_date" : year}).limit(3))
    return Response(200, users).serialize()

# /getByGradDate/<year>/<count>
@api_route.route('/getByGradDate/<int:year>/<int:count>')
def chooseCountGradDate(year, count):
    # Returns array of specified amount of users with specified grad date
    users = list(db.users.find({"grad_date" : year}).limit(count))
    return Response(200, users).serialize()

# ideas
# /getByGradRange
# /getBySkills
