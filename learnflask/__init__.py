from flask import (Flask, request)
from learnflask.blue import bpp
app = Flask(__name__)
app.register_blueprint(bpp, url_prefix='/bpp')

import learnflask.views
