import csv

class Men:
    def __init__(self, firsname, lastname, age):
        self.firsname = firsname
        self.lastname = lastname
        self.age = age

class Bank:
    def __init__(self, name, bid):
       self.name = name
       self.bid = bid
    def WriterMenInfo(self, men):
        myData = [["FirstName", "LastName", "Age", "Bank", "Bid"],
            [men.firsname, men.lastname, men.age, self.name, self.bid]]
            
        myFile = open('WriterInfoMen1.csv', 'w')
        with myFile:
            writer = csv.writer(myFile, delimiter=';')
            writer.writerows(myData)
     
     
    def DictWriterMenInfo(self, men):
        with open('DictWriterMenInfo.csv', 'w') as csvfile:
            fieldnames = ['FirstName', 'LastName', 'Age', 'Bank', 'Bid']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
            writer.writeheader()
            writer.writerow({'FirstName': men.firsname, 'LastName': men.lastname, 'Age': men.age, 'Bank': self.name, 'Bid': self.bid})
       
print('Введите Ваше имя, фамилию, возраст:')

men = Men(firsname=input(), lastname=input(), age=input())
print('Вы: ', men.firsname, men.lastname, men.age)

if men.age < '21':
    print('Извините, но ипотеку Вы можете получить только с 21 года')
    exit(0)

bank1 = Bank("Сбер", "7.7%")
bank2 = Bank("ВТБ", "3.9%")
bank3 = Bank("Росбанк", "5.2%")

print('Доступные банки:')

print(bank1.name, ':', bank1.bid)
print(bank2.name, ':', bank2.bid)
print(bank3.name, ':', bank3.bid)

print('В каком банке вы хотели бы взять ипотеку?')
myBan = input()

if myBan == '1':
    print('Вы выбрали', bank1.name, 'процентная ставка: ', bank1.bid)
elif myBan == '2':
    print('Вы выбрали', bank2.name, 'процентная ставка: ', bank2.bid)
elif myBan == '3':
    print('Вы выбрали', bank3.name, 'процентная ставка: ', bank3.bid)
else:
    print('Выбранного вами банка не существует')
    
print('Просмотреть предложения оставшихся банков? Y/N')
answer = input()

while answer != 'N':

    print('Доступные банки:')

    print(bank1.name, ':', bank1.bid)
    print(bank2.name, ':', bank2.bid)
    print(bank3.name, ':', bank3.bid)

    print('В каком банке вы хотели бы взять ипотеку?')
    myBan = input()   

    if myBan == '1':
        print('Вы выбрали', bank1.name, 'процентная ставка: ', bank1.bid)
    elif myBan == '2':
        print('Вы выбрали', bank2.name, 'процентная ставка: ', bank2.bid)
    elif myBan == '3':
        print('Вы выбрали', bank3.name, 'процентная ставка: ', bank3.bid)
    else:
        print('Выбранного вами банка не существует')
        
    print('Просмотреть предложения оставшихся банков? Y/N')
    answer = input()
      
if answer == 'N':
    
    print('Поздравляем с выбором банка!')
    if myBan == '1':
        print('Запись Ваших данных с помощью csv.writer  .......')
        bank1.WriterMenInfo(men)
        print("Запись прошла успешно!")

    elif myBan == '2':
        print('Запись Ваших данных с помощью csv.writer  .......')
        bank2.WriterMenInfo(men)
        print("Запись прошла успешно!")

    elif myBan == '3':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        bank3.DictWriterMenInfo(men)
        print("Запись прошла успешно!")

print('ВНИМАНИЕ! Только для Вас мы сформировали выгодные кредитные предложения от наших банков-парнеров!!!')
print('Выберите удобный для Вас формат представления данных: 1. Вывод в колонках 2. Вывод в строках ')

myReaderCSV = input()

if myReaderCSV == '1':
    with open('Bank.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
elif myReaderCSV == '2':
    results = []
    with open('Bank.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    print (results)
else:
    exit(0)