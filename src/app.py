from AddressEntry import AddressEntry
from backend.csv import CsvBackend

db = CsvBackend()
db.connect()

def printResults(results):
	print("\n", str(len(results)) + " results found\n")
	for result in results:
		print(result.firstName + " " + result.lastName)
		print(result.street)
		print(result.city + ", " + result.state + " " + result.zip + "\n")

searchTerm = ''

while searchTerm != 'exit':
	searchTerm = input("search addresses: ")
	if searchTerm != 'exit':
		printResults(db.search(searchTerm))
	