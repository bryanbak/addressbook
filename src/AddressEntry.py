class AddressEntry():
	""" Model for an entry in the address book """
	def __init__(self, csvRow):
		self.firstName = csvRow[0]
		self.lastName = csvRow[1]
		self.street = csvRow[2]
		self.city = csvRow[3]
		self.state = csvRow[4]
		self.zip = csvRow[5]