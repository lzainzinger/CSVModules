import csv

__author__ = 'lukaszainzinger'
__date__ = '24-01-2016'
__version__ = '1.0'

"""
    Eine Klasse zum Einlesen, Verarbeiten, Erstellen und Ausgeben von CSV-Files.
"""

class CSVModules():

    """
        :param : filename, der Pfad zum File bzw der Filename
        :param : delimiter, der delimiter des Files
    """

    def __init__(self, filename=None, delimiter=";"):
        self.filename = filename
        self.delimiter = delimiter

    def readCSV(self):
        """
        Methode zum Einlesen eines CSV-Files.
        :return: liste der Eintraege
        """

        content = []
        with open(self.filename) as file:
            sn = csv.Sniffer()
            sn.preferred = [self.delimiter]
            try:
                dialect = sn.sniff(file.read(1024))
            except csv.Error:
                if not file.endswith("csv"):
                    self.delimiter = "\t"
                    file.seek(0)
                    reader = csv.reader(file, delimiter=self.delimiter)
                    dialect = reader.dialect
            file.seek(0)
            reader = csv.reader(file, dialect)
            rownr = 0

            for row in reader:

                if rownr == 0:
                    header = row
                else:
                #    print(row)
                    content.append(row)
                rownr += 1

            file.close()

        return content.copy()

    def writeCSV(self, outfilename, delimiter=';'):
        """
        Methode zum Schreiben eines CSV-Files aus einem anderen CSV-File
        :param outfilename: Pfad bzw Name des Files in dem die Daten gespeichert werden sollen
        :param delimiter: Delimiter welcher beim Output-File verwendet werden soll
        :return:
        """

        input = open(self.filename)
        dialect = csv.Sniffer().sniff(input.read(1024))
        input.seek(0)
        reader = csv.reader(input, dialect)
        out = open(outfilename, "w")
        writer = csv.writer(out, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_ALL)

        for row in reader:
            writer.writerow(row)

        input.close()
        out.close()

def main():
    x = CSVModules("wahl.csv")
    z = x.readCSV()
    x.writeCSV("out.csv", '\t')

main()
