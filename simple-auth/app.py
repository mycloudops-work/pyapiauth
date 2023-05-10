from flask import Flask, request, jsonify, make_response
from msal import PublicClientApplication
import logging

# Optional logging
# logging.basicConfig(level=logging.DEBUG)  # Enable DEBUG log for entire script
logging.getLogger("msal").setLevel(logging.INFO)  # Optionally disable MSAL DEBUG logs



app = Flask(__name__)

authapp = PublicClientApplication("clienid", authority="https://login.microsoftonline.com/tenantid")
result = None

@app.route('/')
def hello_world():
    result = None
    accounts = authapp.get_accounts()
    if accounts:
        # If so, you could then somehow display these accounts and let end user choose
        print("Pick the account you want to use to proceed:")
        for a in accounts:
            print(a["username"])
        # Assuming the end user chose this one
        chosen = accounts[0]
        # Now let's try to find a token in cache for this account
        result = authapp.acquire_token_silent(["User.Read"], account=chosen)
        print("\n the token: " + result)
        # return 'Hello, World!'

    if not result:
        # So no suitable token exists in cache. Let's get a new one from AAD.
        # result = authapp.acquire_token_by_one_of_the_actual_method(..., scopes=["User.Read"])
        result = authapp.acquire_token_interactive(scopes=["User.Read"])
    if "access_token" in result:
        print(result["access_token"])  # Yay!
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))  # You may need this when reporting a bug

@app.route('/login')
def login_world():
        return 'Login, World!'

@app.route('/logout')
def logout_world():
        return 'Logedout, World!'

@app.route('/authok')
def authok_world():
        return 'Authenticated page'


@app.route('/post', methods=['POST'])
def testpost():
    input_data = request.get_json(force=True)
    dictToReturn = {'text':input_data['text']}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=True)