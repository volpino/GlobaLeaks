import gluon.contrib.simplejson as json
from gluon.fileutils import copystream

import os
import shutil

def index():
    return {}



def post():
    # shutil.copyfileobj(request.body, open("/dev/null", "wb"))
    try:
        a = request.body.read()
        return json.dumps({"DIO": "ESISTE"})
    except:
        return json.dumps({"PORCODIO": "LADRO :P"})