import unittest
import server.backend.csv
from server.backend.csv import CsvBackend
from AddressEntry import AddressEntry

class CsvBackendTests(unittest.TestCase):
	def setUp(self):
		self.csvBackend = CsvBackend()
		entry = AddressEntry()
		row = []
		row.append("Bryan")
		row.append("Bakotich")
		row.append("4822 2nd Ave.")
		row.append("Tacoma")
		row.append("WA")
		row.append("18")
		server.backend.csv.populateEntryFromCsvRow(entry, row)
		self.csvBackend.addressEntries.append(entry)
		
	def test_removePunctuation(self):
		punctuationRemoved = server.backend.csv.removePunctuationAndLowercase("This, had  #punctuation.    ")
		self.assertEqual(punctuationRemoved, "this had punctuation")
		
	def test_lastname_search(self):
		results = self.csvBackend.search("Bakotich")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("Bokotih")
		self.assertEqual(len(results), 0)
		
	def test_partial_lastname_search(self):
		results = self.csvBackend.search("Bako")
		self.assertEqual(len(results), 1)
		
	def test_case_insensitive_search(self):
		results = self.csvBackend.search("bakotich")
		self.assertEqual(len(results), 1)
		
	def test_fullname_search(self):
		results = self.csvBackend.search("bryan   bakotich")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("bakotich, bryan")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("bakotich bryan")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("bakotich brian")
		self.assertEqual(len(results), 0)
		
	def test_city_state_search(self):
		results = self.csvBackend.search("tacoma")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("tacoma, wa")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("wa")
		self.assertEqual(len(results), 1)
		
	def test_street_search(self):
		results = self.csvBackend.search("4822  2nd ave")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("4822")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("2nd ave")
		self.assertEqual(len(results), 1)
		
	def test_dave(self):
		""" searching for dave was returning people with 2nd ave addresses """
		results = self.csvBackend.search("dave")
		self.assertEqual(len(results), 0)
		
	@unittest.skip("this is not implemented yet")
	def test_abbreviations(self):
		results = self.csvBackend.search("ave")
		self.assertEqual(len(results), 1)
		results = self.csvBackend.search("avenue")
		self.assertEqual(len(results), 1)
		
if __name__ == '__main__':
	unittest.main()