# write a program using csv.writer for writing csv files in python
import csv
with open('hollywood.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Character_name', 'Character_age', 'Series'])
    writer.writerow(['Ian Somerhalder ',  'Damon Salvatore ',
                    41, ' The Vampire Diaries'])
    writer.writerow(['Noah Schnapp ',  'Will Byers ', 16, ' Stranger Things'])
    writer.writerow(['Daniel Radcliffe ', 'Harry potter ',
                    17, ' Harry potter series'])
    writer.writerow(['Park Solomon ', 'Lee Suhyeok ',
                    17, ' All of us are dead'])
    writer.writerow(['Song Hye-kyo ', 'Moon Dong-Eun ', 34, ' The Glory'])
    writer.writerow(['Wo Do-hwan ', 'Hae Jo ', 30, ' Mr. Plankton'])

# write a program using csv.reader for reading csv files in python


def print_table(rows):
    # calculate column widths
    widths = [max(len(str(x)) for x in col) for col in zip(*rows)]
    # header
    header = rows[0]
    print(" | ".join(str(v).ljust(w) for v, w in zip(header, widths)))
    print("-+-".join("-"*w for w in widths))
    # rows
    for r in rows[1:]:
        print(" | ".join(str(v).ljust(w) for v, w in zip(r, widths)))


with open('hollywood.csv', newline='') as f:
    reader = list(csv.reader(f))
    print_table(reader)

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


def print_table(rows):
    # calculate column widths
    widths = [max(len(str(x)) for x in col) for col in zip(*rows)]
    # header
    header = rows[0]
    print(" | ".join(str(v).ljust(w) for v, w in zip(header, widths)))
    print("-+-".join("-"*w for w in widths))
    # rows
    for r in rows[1:]:
        print(" | ".join(str(v).ljust(w) for v, w in zip(r, widths)))


with open('data_dict.csv', newline='') as f:
    reader = list(csv.reader(f))
    print_table(reader)
