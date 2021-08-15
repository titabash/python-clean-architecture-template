from flask import Flask, request, Blueprint
import os
import yaml
import sys

sys.path.append('./')


# Load Env
try:
    # local
    with open('/service/src/env.yml') as f:
        os.environ.update(yaml.load(f, Loader=yaml.FullLoader))
except FileNotFoundError:
    os.environ["ENV"] = "Local"
    # Google Cloud Functions
    pass

WEBHOOK_URL = os.getenv('WEBHOOK_URL')

main_module = Blueprint("main", __name__)

# Setup to use Restful API


@main_module.route("/", methods=["GET", "POST"])
def hello_web():
    text = f'Hello API from {os.environ["ENV"]} using Python {sys.version} !, {request.args.get("test")}, {request.get_data()}'
    print(text)
    print(request.args.get("test"))  # Query Param
    print(request.get_data())  # Request Body
    return text


port = int(os.environ.get('PORT', 8000))
if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(main_module)
    app.run('0.0.0.0', port, debug=True)
