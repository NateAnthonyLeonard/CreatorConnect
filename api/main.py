import platform, os
from api_main import app

app.run(host="localhost", port=5000, debug=True)

if (platform.system() == "Windows"):
   cmd = "set"
else:
    cmd = "export" 

os.system("{} FLASK_APP=api_main.py".format(cmd))
os.system("{} FLASK_ENV=development".format(cmd))
app.run()
