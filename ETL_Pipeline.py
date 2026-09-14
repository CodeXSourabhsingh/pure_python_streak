import csv
class DataExtractor:
    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self):
        try:
            with open(self.filepath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                raw_data = list(reader)
                print(f"Extracted {len(raw_data)} rows from {self.filepath}")
                return raw_data
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
            return []

class DataTransformer:  
    def __init__(self, raw_data):   
        self.raw_data = raw_data

    def transform(self):
        clean_data = []
        seen = set()
        for row in self.raw_data:
            row['name'] = row['name'].strip().lower()
            row['city'] = row['city'].strip().lower()
            
            try:
                row['age'] = int(row['age'])
                row['glucose'] = float(row['glucose'])
            except ValueError:
                continue   # Skip row if conversion fails

          
            if not row['name'] or not row['city']:
                continue

            key = (row['name'], row['age'], row['glucose'])
            if key in seen:
                continue

            seen.add(key)
            clean_data.append(row)

        return clean_data

class DataLoader:
    def __init__(self, output_filepath):
        self.output_filepath = output_filepath

    def loader(self, data):
        if not data:
            print("No clean data to write.")
            return
        try:
            with open(self.output_filepath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                print(f"Success: {len(data)} rows loaded to {self.output_filepath}")
        except PermissionError:
            print('Error: File is open in another program. Close it and try again.')
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    extractor = DataExtractor('patient_data.csv')
    raw_data = extractor.extract()

    if raw_data:
        transformer = DataTransformer(raw_data)   # Fixed name
        clean_data = transformer.transform()

        if clean_data:
            loader = DataLoader('clean_patient_data.csv')
            loader.loader(clean_data)