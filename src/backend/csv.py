import csv
import re
from AddressEntry import AddressEntry

def removePunctuationAndLowercase(stringWithPunc):
	# first get rid of all non word/space chars
	noPunc = re.sub(r"[^\w\s]", "", stringWithPunc)
	# collapse consecutive spaces into a single space
	collapseSpaces = re.sub(r"\s\s+", " ", noPunc)
	return collapseSpaces.lower().strip()
	
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
	return removePunctuationAndLowercase(" ".join(addressArray))
	
def populateEntryFromCsvRow(entry, row):
	entry.firstName = row[0]
	entry.lastName = row[1]
	entry.street = row[2]
	entry.city = row[3]
	entry.state = row[4]
	entry.zip = row[5]
	# This is the string we'll be searching on
	entry.addressString = getCombinedAddress(entry)

class CsvBackend():
	""" Reads Address data from address_book.csv file and makes it searchable """
	def __init__(self):
		self.addressEntries = []
	
	def connect(self):
		# parse the csv file
		addressFile = CsvFileNormalizer("address_book.csv")
		csvReader = csv.reader(addressFile, delimiter=',', quotechar='"')
		for row in csvReader:
			entry = AddressEntry()
			populateEntryFromCsvRow(entry, row)
			self.addressEntries.append(entry)
	
	def search(self, st):
		results = []
		searchTermNoPunc = removePunctuationAndLowercase(st)
		for entry in self.addressEntries:
			if searchTermNoPunc in entry.addressString:
				results.append(entry)
		return results

class CsvFileNormalizer():
	""" Iterator that preprocesses lines in the csv file to ensure consistent quotes """
	def __init__(self, fileName):
		self.fileReader = open(fileName, "r", newline="")
		
	def __iter__(self):
		return self
		
	def __next__(self):
		line = self.fileReader.readline()
		if line == "":
			self.fileReader.close()
			raise StopIteration
		return line.replace("“", "\"")
