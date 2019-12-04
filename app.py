from flask import Flask, render_template, session, url_for, request, redirect, flash
from os import urandom
import pymysql

app = Flask(__name__)
app.secret_key = urandom(24)

def getAccounts():
	password = [
		'Swampert27'
	]
	connection = pymysql.connect(host='localhost', user='Gudmundur', password=password[0], db='Vefth', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	sql = connection.cursor()
	sql.execute('select * from users;')
	accounts = sql.fetchall()
	connection.close()
	
	session['user_ids'] = {}
	session['usernames'] = []
	for x in accounts:
		print(x)
		session['usernames'].append(x['name'])
		session['user_ids'][x['name']] = x['user_id']

	return accounts

def getMesseges(id, poster=False):
	password = [
		'Swampert27'
	]
	connection = pymysql.connect(host='localhost', user='Gudmundur', password=password[0], db='Vefth', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	sql = connection.cursor()

	if poster:
		sql.execute(f'select * from messeges where user = {id};')
	else:
		sql.execute(f'select * from messeges where poster = {id};')
	
	return(sql.fetchall())

def saveMessege(id, messege, poster):
	password = {
		'password':'Swampert27'}
	connection = pymysql.connect(host='localhost', user='Gudmundur', password=password['password'], db='Vefth', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	sql = connection.cursor()
	sql.execute(f'insert into messeges(user, messege, poster) values({id}, "{messege}", {poster});')
	connection.commit()
	connection.close()

def delMessege(id):
	password = {
		'password':'Swampert27'}
	connection = pymysql.connect(host='localhost', user='Gudmundur', password=password['password'], db='Vefth', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	sql = connection.cursor()
	sql.execute(f'delete from messeges where id = {id};')
	connection.commit()
	connection.close()

def changeMessege(id, messege):
	password = {
		'password':'Swampert27'}
	connection = pymysql.connect(host='localhost', user='Gudmundur', password=password['password'], db='Vefth', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	sql = connection.cursor()
	sql.execute(f"update messeges set messege = '{messege}' where id = {id};")
	connection.commit()
	connection.close()
	

@app.route("/", methods=['POST', 'GET'])
def home():
	error = False
	if request.method == 'POST':
		session['user'] = request.form.get('username')
		session['password'] = request.form.get('password')

		for account in getAccounts():
			if account['name'] == session['user'] or account['email'] == session['user']:
				if account['password'] == session['password']:
					flash("Innskráning tókst!")
					session['id'] = int(account['user_id'])
					return redirect(url_for('messeges'))
		
		error = True
		
	return render_template('innskraning.html', error=error)

@app.route("/new", methods=['POST', 'GET'])
def newSqlUser():
	errors = [False, False]
	if request.method == 'POST':
		session['user'] = request.form.get('username')
		session['password'] = request.form.get('password')
		session['email'] = request.form.get('email')

		for account in getAccounts():
			if account['name'] == session['user']:
				errors[0] = True

			if account['email'] == session['email']:
				errors[1] = True

		if not errors[0] and not errors[1]:
			password=[
				'Swampert27'
			]
			connection = pymysql.connect(host='localhost', user='Gudmundur', password=password[0], db='Vefth', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
			command = f"insert into users(name, password, email)\nValues('{ session['user'] }', '{ session['password'] }', '{ session['email'] }');"
			sql = connection.cursor()
			sql.execute(command)
			connection.commit()
			connection.close()
			accounts = getAccounts

			return redirect(url_for('home'))

	return render_template('nyskranning.tpl', errors=errors)

@app.route("/signedIn/home")
def messeges():
	return render_template('messeges.tpl', messeges=getMesseges(session['id']), usernames=session['usernames'], changes=False)

@app.route("/signedIn/sent")
def sent():
	return render_template('messeges.tpl', messeges=getMesseges(session['id'], True),usernames=session['usernames'], changes=True)

@app.route("/signedIn/send", methods=['POST', 'GET'])
def send():
	if request.method == 'POST':
		messege = request.form.get('messege')
		receiver = session['user_ids'][request.form.get('receiver')]

		saveMessege(session['id'], messege, receiver)
		return redirect(url_for('sent'))

	return render_template('send.tpl', messeges=getMesseges(session['id']), sending=True)

@app.route("/signedIn/change/<int:id>", methods=['POST', 'GET'])
def change(id):
	if request.method == 'POST':
		messege = request.form.get('messege')
		changeMessege(id, messege)
		return redirect(url_for("sent"))

	return render_template('send.tpl', sending=False)

@app.route("/signedIn/delete/<int:id>")
def delete(id):
	print(id)
	delMessege(id)
	return redirect(url_for("sent"))

if __name__ == '__main__':
	app.run(debug=True)