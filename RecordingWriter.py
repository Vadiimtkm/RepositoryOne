import csv
 
myData = [["name_fuel", "price"],
          ['AI-92', '40.20'],
          ['AI-95', '45.45'],
          ['diesel', '50.34']]
 
myFile = open('laba3(testtoplivo2).csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(myData)
     
print("Writing complete")