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
	
	def connect(self):
		addressFile = CsvFileNormalizer("address_book.csv")
		csvReader = csv.reader(addressFile, delimiter=',', quotechar='"')
		for row in csvReader:
			entry = AddressEntry()
			entry.firstName = row[0]
			entry.lastName = row[1]
			entry.street = row[2]
			entry.city = row[3]
			entry.state = row[4]
			entry.zip = row[5]
			entry.addressString = getCombinedAddress(entry)
			self.addressEntries.append(entry)
	
	def search(self, st):
		results = []
		searchTermNoPunc = removePunctuationAndLowercase(st)
		for entry in self.addressEntries:
			if searchTermNoPunc in entry.addressString:
				print("search: " + searchTermNoPunc)
				print("entry: " + entry.addressString)
				results.append(entry)
		return results

class CsvFileNormalizer():
	def __init__(self, fileName):
		self.fileReader = open(fileName, 'r', newline='')
		
	def __iter__(self):
		return self
		
	def __next__(self):
		line = self.fileReader.readline()
		if line == '':
			self.fileReader.close()
			raise StopIteration
		return line.replace("“", "\"")
