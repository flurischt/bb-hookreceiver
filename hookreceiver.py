"""
a small webapp to receive bitbucket POST hooks.

checkout https://confluence.atlassian.com/display/BITBUCKET/POST+hook+management
see tests.py for an example json request

you'll need to export HOOKRECEIVER_CONFIG_FILE=path/to/config.cfg before running this

"""
import json, os
from flask import Flask, request


app = Flask(__name__)
if 'HOOKRECEIVER_CONFIG_FILE' in os.environ:
    app.config.from_envvar('HOOKRECEIVER_CONFIG_FILE')
else:
    app.config.from_pyfile('config.cfg')


@app.route('/repo/<repo_name>/<token>',  methods=['POST'])
def receive(repo_name, token):
    repo_config = app.config['REPOSITORIES'][repo_name]
    if not repo_config:
        return 'endpoint not configured'
    data = json.loads(request.data)
    return repo_config['handle'](token, data)


@app.route('/repo/<repo_name>')
def receive_without_token(repo_name):
    return receive(repo_name, '')


if __name__ == '__main__':
    app.run(debug=True)
