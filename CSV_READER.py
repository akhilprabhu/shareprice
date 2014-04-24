#!/usr/bin/python
import csv

class CsvLoader():
    SHARE_IN_COMP_A  = 0
    SHARE_IN_COMP_B  = 0
    SHARE_IN_COMP_C  = 0
    SHARE_IN_COMP_D  = 0
    HEADER_COUNT = 0
    COMPANIES = [
        {"COMPANY":"A", "ROW":"2", "DEFAULT":"0"},
        {"COMPANY":"B", "ROW":"3", "DEFAULT":"0"},
        {"COMPANY":"C", "ROW":"4", "DEFAULT":"0"},
        {"COMPANY":"D", "ROW":"5", "DEFAULT":"0"},
    ]
    def __init__(self, company=None,year=None, month=None, highest=None):
        self.year = year
        self.month = month
        self.company = company
        self.highest= highest

    def displayHighest(self):
        print "COMPANY: ", self.company, " | YEAR : ", self.year,  " | MONTH: ", self.month,  " | HIGHEST: ", self.highest

    def csv_reader(self, file_obj):
        """
        Read a csv file
        """
        reader = csv.reader(file_obj)

        for j, row in enumerate(reader):
            # CODE to skip the Headers
            if j in range(CsvLoader.HEADER_COUNT):
                pass
            else:
                # Fetch values to parse
                for row in reader:
                    if not int(CsvLoader.SHARE_IN_COMP_A) > int(row[2]):
                        comp1 = CsvLoader("A", row[0],row[1],row[2])
                        CsvLoader.SHARE_IN_COMP_A = row[2]
                    if not int(CsvLoader.SHARE_IN_COMP_B) > int(row[3]):
                        comp2 = CsvLoader("B", row[0],row[1],row[3])
                        CsvLoader.SHARE_IN_COMP_B = row[3]
                    if not int(CsvLoader.SHARE_IN_COMP_C) > int(row[4]):
                        CsvLoader.SHARE_IN_COMP_C = row[4]
                        comp3 = CsvLoader( "C", row[0],row[1],row[4])
                    if not int(CsvLoader.SHARE_IN_COMP_D) > int(row[5]):
                        CsvLoader.SHARE_IN_COMP_D = row[5]
                        comp4 = CsvLoader("D", row[0],row[1],row[5])

        comp1.displayHighest()
        comp2.displayHighest()
        comp3.displayHighest()
        comp4.displayHighest()

if __name__ == "__main__":
    csv_loader = CsvLoader()
    # File path on same directory
    file_path = "data_upload_sample.csv"
    with open(file_path, "rb") as file_obj:
        csv_loader.csv_reader(file_obj)