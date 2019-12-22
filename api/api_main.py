import os
import sys
import configparser
from flask import Blueprint
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, OperationFailure

# init api subroute
api_route = Blueprint('api', __name__, url_prefix="/api")

# Read Config
config = configparser.ConfigParser()
conf_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../config.ini")
config.read(conf_file)

# Init MongoDB Connection and run sample query to test authentication
uri = config['MongoDB']['URI']
try:
    mongo = MongoClient(uri)
    db = mongo['CreatorConnect']
    list(db.users.find({}).limit(1))
except ConfigurationError as err:
    if (err.args[0] == "A DNS label is empty."):
        print("[ERROR]: MongoDB URI returning SRV error. If you're on the FSUSecure")
        print("         network, we recommend using the expanded URI to circumvent")
        print("         this error.")
    sys.exit(1)
except OperationFailure as err:
    if (err.args[0] == "bad auth Authentication failed."):
        print("[ERROR]: MongoDB URI returning authentication error. Make sure you")
        print("         are using a URI with a valid username/password combo.")
    sys.exit(1)

# Now that api is initialized, import other paths
# Import all get requests
import api.api_gets

# Other handlers
@api_route.route("/<path:invalid_path>")
def api_404(invalid_path):
    return "Error 404", 404
