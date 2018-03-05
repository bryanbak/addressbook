from cement.core.foundation import CementApp
from AddressEntry import AddressEntry
from backend.csv import CsvBackend

# Get an instance of the backend and connect
# This would be better if it was an HTTPClient making
# queries to the server component rather than being coupled
# with the server code
db = CsvBackend()
db.connect()

def printResults(results):
	print("\n", str(len(results)) + " results found\n")
	for result in results:
		print(result.firstName + " " + result.lastName)
		print(result.street)
		print(result.city + ", " + result.state + " " + result.zip + "\n")

with CementApp("addressbook") as app:
	app.setup()
	
	# define command line args the app will accept
	app.args.add_argument("-i", "--interactive", action="store_true", dest="interactive", help="interactive mode")
	app.args.add_argument("extra_arguments", action="store", nargs="*")
	
	app.run()
	
	# interactive mode. prompt user for input in a loop until
	# we receive the 'exit' command
	if app.pargs.interactive:
		print("Running addressbook lookup in interactive mode")
		print("Type 'exit' to exit the program\n")
		
		searchTerm = ""

		while True:
			searchTerm = input("search addresses: ")
			if searchTerm == "exit":
				break
			printResults(db.search(searchTerm))
	else:
		searchTerm = app.pargs.extra_arguments[0]
		printResults(db.search(searchTerm))