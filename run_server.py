from flask import Flask, current_app
from flask_cors import CORS as cors
from api.api_main import api_route

# Init Flask App
app = Flask(__name__, static_url_path='', static_folder='webapp/build')
cors(app)

# init routes
app.register_blueprint(api_route)

@app.route("/", defaults={'non_api_path': ''})
@app.route("/<path:non_api_path>")
def main(non_api_path):
    return current_app.send_static_file('index.html')

# run app
if __name__ == '__main__':
    app.run()
