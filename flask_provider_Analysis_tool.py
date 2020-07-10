from lti.contrib.flask import FlaskToolProvider
from oauthlib.oauth1 import RequestValidator
from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = '12345678-8137-2FF2-D206'
key = '12345678-8137-2FF2-ABCD'
the_secret = 'sd54f65sd65f6sde'

class MyRequestValidator(RequestValidator):
    # enforce_ssl = True  # default False
    client_key_length = (3, 50)
    nonce_length = (13, 50)
    dummy_client = ''  # Need to watch for this one

    def validate_timestamp_and_nonce(*args, **kwargs):
        # Validate the nonce here
        return True

    def validate_client_key(self, client_key, request):
        return client_key == key

    def get_client_secret(self, client_key, request):
        # Always return a secret, even if the client key is bad.
        # OAuthlib still runs the validation steps to avoid timing attacks.
        return the_secret if client_key != self.dummy_client else ''  # dummy secret

@app.route('/', methods=['GET', 'POST'])
#@lti(request='session', app=app , role='staff')
#def index(course_id=None, user_id=None, lti=lti):
def test():
    tool_provider = FlaskToolProvider.from_flask_request(request=request)
    temp = tool_provider.launch_params.__dict__['_params']['context_label']
    return redirect('.......&var-flask_test=' + temp+'&refresh=1m')


if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8090)

# git20200710
