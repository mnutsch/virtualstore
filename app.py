from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'



@app.route('/', methods=['GET', 'POST']) # The acceptable HTTP methods for this
def index():
	#return 'Hello World!'
    return render_template('virtualstore.html')


# @app.route('public/<path:path>')
# def send_js(path):
#     return send_from_directory('public', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)