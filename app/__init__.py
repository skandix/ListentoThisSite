from flask import Flask


from app.root.controllers import root
from app.status.controllers import status

app = Flask(__name__)

app.register_blueprint(root, url_prefix='/')
app.register_blueprint(status, url_prefix='/stat')
