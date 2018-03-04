import unittest
import backend.csv
from backend.csv import CsvBackend

class CsvBackendTests(unittest.TestCase):
	def test_something(self):
		punctuationRemoved = backend.csv.removePunctuationAndLowercase("This, had #punctuation.")
		self.assertEqual(punctuationRemoved, "thishadpunctuation")
		
if __name__ == '__main__':
	unittest.main()