from flask import request

@app.route('/get_data', methods=['POST'])
def addContent():
	print("I got it")
	print(request.form['firstName'])