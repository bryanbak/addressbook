import csv
import re
from AddressEntry import AddressEntry

def removePunctuationAndLowercase(stringWithPunc):
	return re.sub(r'[^\w]', '', stringWithPunc).lower()
	
def getCombinedAddress(addressEntry):
	addressArray = [
		addressEntry.firstName,
		addressEntry.lastName,
		addressEntry.firstName,
		addressEntry.street,
		addressEntry.city,
		addressEntry.state,
		addressEntry.zip
	]
	return removePunctuationAndLowercase(''.join(addressArray))

class CsvBackend():
	""" Reads Address data from address_book.csv file """
	def __init__(self):
		self.addressEntries = []
		with open('address_book.csv', newline='') as addressFile:
			csvReader = csv.reader(addressFile, delimiter=',', quotechar='"')
			for row in csvReader:
				entry = AddressEntry(row)
				entry.addressString = getCombinedAddress(entry)
				self.addressEntries.append(entry)

	def search(self, st):
		results = []
		searchTermNoPunc = removePunctuationAndLowercase(st)
		for entry in self.addressEntries:
			if searchTermNoPunc in entry.addressString:
				results.append(entry)
		return results
