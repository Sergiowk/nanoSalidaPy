from flask import Flask, jsonify

#Initialize the application
app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return jsonify({'Message': 'Welcome, the API Server is running'})

#Run the application
if __name__=="__main__":
    app.run(debug=True)