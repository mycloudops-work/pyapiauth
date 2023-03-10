# pyapiauth
Python API build with Oauth2 security

## Setup
- Virtual env: ./venv_pyapiauth
- .gitignore:
    - venv_*
- requirements.txt - add all the libraries to requirements files

# Step 1: Build Flash Python API

How to Create an API Using The Flask Framework - https://nordicapis.com/how-to-create-an-api-using-the-flask-framework/
- [code files in this direcotry](/simple-flask-api/)

# Step 2: Secure API with Auth (Auth0 by okta)
Add Authorization to a Flask API application - https://auth0.com/docs/quickstart/backend/python/interactive
- [code files in this directory](/backend-flask-api-auth/)

- Register an API in auth0 IDP - https://auth0.com/docs/get-started/auth0-overview/set-up-apis
``` shell
Name: pyapi-backend
Identifier: http://localhost:5000/api
Signing Algorithm: RS256
```

# Step 3: Secure API with Azure AD
- Python Azure Function Web API secured by Azure AD - https://github.com/Azure-Samples/ms-identity-python-webapi-azurefunctions
- Validating JSON web tokens (JWTs) from Azure AD, in Python - https://robertoprevato.github.io/Validating-JWT-Bearer-tokens-from-Azure-AD-in-Python/

# reference
- The ultimate Python library in building OAuth and OpenID Connect servers - https://authlib.org/ 
- JWT creation and validation in Python using Authlib - https://www.scottbrady91.com/python/authlib-python-jwt
- Python API: Authorisation - https://auth0.com/docs/quickstart/backend/python