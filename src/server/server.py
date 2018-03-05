from flask import Flask
from flask import jsonify
from flask import request

from backend.csv import CsvBackend

app = Flask(__name__)

db = CsvBackend()
db.connect()

@app.route("/")
def search():
	searchTerm = request.args.get('st')
	results = db.search(searchTerm)
	return jsonify([r.serialize() for r in results])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)