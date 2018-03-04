import csv
from AddressEntry import AddressEntry

class CsvBackend():
	""" Reads Address data from address_book.csv file """
	def __init__(self):
		self.addressEntries = []
		with open('address_book.csv', newline='') as addressFile:
			csvReader = csv.reader(addressFile, delimiter=',', quotechar='"')
			for row in csvReader:
				entry = AddressEntry(row)
				self.addressEntries.append(entry)

	def search(self, st):
		results = []
		for entry in self.addressEntries:
			if entry.lastName == st:
				results.append(entry)
		return results