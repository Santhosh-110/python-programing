# from flask_ import Flask
# app = Flask(__name__)
# @app.route("/",methods = ['GET'])
# def trail():
#     return "wellcome to all"
# if __name__ == "__flask___":
#     app.run(debug = "True")


# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def trail():
#     return "Welcome to all"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask,jsonify
# app=Flask(__name__)

# data={
#     "1":{"name":"santhosh","age":27},
#     "2":{"name":"Rohan","age:":23}
# }

# @app.route("/",methods=['GET'])
# def get_user():
#     return jsonify(data)

# if __name__ == "__flask__":
#     app.run(debug=True)


from flask import Flask,jsonify,request
app = Flask(__name__)

data = {
    "1":{"name":"Deva","age":19},
    "2":{"name":"santhosh","age":23}
} 

@app.route("/user",methods=['GET'])
def get_user():
    return jsonify(data)

@app.route("/user/<user_id>",methods=['GET'])
def get_users(user_id):
    user = data.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"Error":"User not found"})

if __name__ == "___main__":
    app.run(debug=True)
