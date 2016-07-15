from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/logit', methods=['GET', 'POST'])
def logit():
    import q; q(request.data)
