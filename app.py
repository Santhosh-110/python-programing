from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_get', methods=['GET'])
def handle_get():
    print("Received GET request")
    name = request.args.get('Username')
    pas = request.args.get('password')
    mail = request.args.get('Email')
    
    # Handle missing values gracefully
    if not name or not pas or not mail:
        return jsonify({'error': 'Missing required parameters'}), 400

    print(f"the name is: {name}")
    print(f"the password is: {pas}")
    print(f"the email is: {mail}")
    return jsonify({'Username': name, 'password': pas, 'Email': mail})

@app.route('/handle_post', methods=['POST'])
def handle_post():
    # Use .get() to avoid KeyError if any field is missing
    name = request.form.get('Username')
    pas = request.form.get('password')
    mail = request.form.get('Email')

    # Check if fields are missing and handle accordingly
    if not name or not pas or not mail:
        return jsonify({'error': 'Missing required fields'}), 400

    print(name, pas, mail)
    return jsonify({'Username': name, 'password': pas, 'Email': mail})


@app.route('/home', methods=['GET'])
def home():
    return jsonify({"name": "asd", "pass": "123asd", "email": "asd@gmail.com"})

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/home")
def home():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True)