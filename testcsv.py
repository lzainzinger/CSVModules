from unittest import TestCase
import CSVModules_GIT.CSVModules


class TestCSV(TestCase):
    def setUp(self):
        file1 = "wahl.csv"
        file2 = "false.csv"
        self.csv = CSVModules(file1)
        self.csvfalse = CSVModules(file2)

        self.d1 = ';'
        self.d2 = ','

        self.r1 = self.csv.readCSV()
        self.r2 = self.csv.readCSV()

        self.read_test = ['SPOE', 'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE']
        self.out_test = [['SPOE', 'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE'], ['27', '14', '15', '10', '9', '0', '1', '0', '0', '0', '0', '0']]

        pass

    def test_cantreadCSV(self):
        self.assertRaises(FileNotFoundError, self.csvfalse.readCSV())

    def test_readCSV(self):
        reader = self.csv.readCSV()
        for row in reader:
            assert(row == self.read_test)

    def test_cantwriteCSV(self):
        self.assertRaises(TypeError, self.csv.writeCSV("xy.csv"))

