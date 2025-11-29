# write a program using csv.writer for writing csv files in python
import csv
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Gojo', 30, 'Tokyo'])
    writer.writerow(['Sinchan', 5, 'Kasukabi'])
    writer.writerow(['Naruto', 50, 'Hidden life in village'])
    writer.writerow(['luffy', 19, 'goa kindom'])
# write a program using dictornary writer to as a dictonary for writing csv files in python
with open('data_dict.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Gojo', 'Age': 30, 'City': 'Tokyo'})
    writer.writerow({'Name': 'Sinchan', 'Age': 5, 'City': 'Kasukabi'})
    writer.writerow({'Name': 'Naruto', 'Age': 50,
                    'City': 'Hidden life in village'})
    writer.writerow({'Name': 'luffy', 'Age': 19, 'City': 'goa kindom'})
