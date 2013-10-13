from flask import Blueprint
# access static files: /bpp/static/ ; "bpp" is the registered prefix
# the template_folder has a lower priority than the app's
# so, the blue/templates/index.html won't be found
bpp = Blueprint('bpp', __name__, static_folder='static', \
        template_folder='templates')

import learnflask.blue.views
