from flask import Flask, request, jsonify

app = Flask(__name__)

#################################### Get Rules ##############################################

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# Note the ?, anything after that is your Query Perameter
# "/get-user/123?extra=hello" 

#################################### Post Rules ##############################################

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

#################################### Run App##############################################


if __name__ == '__main__':
    app.run(debug=True)