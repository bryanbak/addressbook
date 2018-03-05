class AddressEntry():
	""" Model for an entry in the address book """
	def __init__(self):
		self.firstName = ""
		self.lastName = ""
		self.street = ""
		self.city = ""
		self.state = ""
		self.zip = ""
		
	def serialize(self):
		return {
			"firstName": self.firstName,
			"lastName": self.lastName,
			"street": self.street,
			"city": self.city,
			"state": self.state,
			"zip": self.zip
		}