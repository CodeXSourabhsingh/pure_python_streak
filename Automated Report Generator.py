import csv
import datetime
class DataReader:
    def __init__(self,filepath):
        self.filepath = filepath
    def read(self):
        try:
            with open(self.filepath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                return data
        except FileNotFoundError:
            print('File not found')
            return[]
class Reporter:
    def __init__ (self,data):
        self.data = data
    def generate(self):
        if not self.data :
            return 'No Data'
        total = len(self.data)
        ages = [int(row['age']) for row in self.data]
        glucose = [float(row['glucose']) for row in self.data]
        avg_age = sum(ages)/total
        avg_glucose = sum(glucose)/total
        highest = max(glucose)
        lowest = min(glucose)
        report = f"""\nPATIENT DATA REPORT\nGenerated: {datetime.datetime.now()}
        Total Patients: {total}\nAverage Age: {avg_age:.2f}
        Average Glucose: {avg_glucose:.2f}
        Highest Glucose: {highest}
        Lowest Glucose: {lowest}"""
        return report

class ReportSaver:
    def __init__(self,filepath):
        self.filepath = filepath
    def save(self,text):
        with open(self.filepath , 'w', newline='') as file:
            file.write(text)
        print("Report Saved")

if __name__ == "__main__":
    reader = DataReader('clean_patient_data.csv')
    data = reader.read()
    if data:
        generator = Reporter(data)
        report = generator.generate()
        saver = ReportSaver('patient_report.txt')
        saver.save(report)

        
