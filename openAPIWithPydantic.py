from flask import Flask, request, jsonify
from pydantic import BaseModel
from flask_pydantic_spec import FlaskPydanticSpec, Response

app = Flask(__name__)
spec = FlaskPydanticSpec('test_api', title='My API', version='1.0.0', servers=[{'url': 'http://localhost:5000'}])

class User(BaseModel):
    name: str
    email: str

@app.route('/user', methods=['POST'])
@spec.validate(body=User, resp=Response(HTTP_200=User))
def create_user():
    data = request.json
    user = User(**data)
    # save user to database or do other things
    return jsonify(user.dict())

@app.route('/delete', methods=['DELETE'])
def delete_user():
    resp = {
        "message" : "deleted user"
    }
    return resp

# app = spec.register(app)

if __name__ == '__main__':
    spec.register(app)
    app.run()
