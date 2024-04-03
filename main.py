# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/shantanu', methods=['GET', 'POST'])
# def greet_shantanu():
#     if request.method == 'GET':
#         name = request.args.get('name', 'Shantanu')
#     elif request.method == 'POST':
#         name = request.form.get('name', 'Shantanu')
    
#     return f"Hello, {name}!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, request

app = Flask(__name__)

@app.route('/shantanu', methods=['GET'])
def greet():
    name = request.args.get('name', '')  # Get the 'name' parameter from the URL
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Listen on all network interfaces
