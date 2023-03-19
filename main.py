from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#@app.route("/")
#def main():
#	return render_template("login.html")


#@app.route("/submit", methods=["POST","GET"])
#def submit():
#	if request.method=="POST":
#		nama=request.form['nama']
#		wa=request.form['wa']
#		"""
#	#	cur = mydb.cursor()
#	#	cur.execute("INSERT INTO data_user(nama, coment) VALUES (%s, %s)", (name, forum))
#		mydb.commit()
#		cur.close()
#		"""
#		print(nama,wa)
#		return render_template("login.html")

#		
#	
#	else :
#		nama=request.args.get('nama')
#		wa=request.args.get('wa')
#		print(nama,wa)
#		return 'Success'
		
@app.route("/")
def main():
	return render_template("login.html")

#@app.route('/submit', methods=['POST'])
#def submit():
#    data = request.get_json()
#    nama = data['nama']
#    wa = data['wa']
#    print(name,age)
#    # Do something with the input data
#    return jsonify({'status': 'success'})
   
@app.route('/input', methods=['POST','GET'])
def input():
  inputValueNama = request.form['inputValueNama']
  
  # kode untuk memproses nilai input
  print(inputValueNama)
  
  response = {'success': True}
  return jsonify(response)


  
if __name__ =="__main__":
	app.run(debug=True)