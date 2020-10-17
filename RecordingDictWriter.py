import csv
 
with open('laba3(testtoplivoDickWriter).csv', 'w') as csvfile:
    fieldnames = ['name_fuel', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
    writer.writeheader()
    writer.writerow({'name_fuel': 'AI-92', 'price': '40.20'})
    writer.writerow({'name_fuel': 'AI-95',
                     'price': '45.45'})
    writer.writerow({'name_fuel': 'AI-98', 'price': '69.10'})
    writer.writerow({'name_fuel': 'diesel', 'price': '50.34'})
 
print("Writing complete")