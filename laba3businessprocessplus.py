import csv

class Men:
    def __init__(self, firsname, lastname, age):
        self.firsname = firsname
        self.lastname = lastname
        self.age = age

print('Введите Ваше имя, фамилию, возраст:')

men = Men(firsname=input(), lastname=input(), age=input())
print('Вы: ', men.firsname, men.lastname, men.age)

if men.age < '21':
    print('Извините, но ипотеку Вы можете получить только с 21 года')
    exit(0)

class Bank:
   def __init__(self, namebankOne, namebankTwo, namebankThree):
       self.namebankOne = namebankOne
       self.namebankTwo = namebankTwo
       self.namebankThree = namebankThree

bank = Bank("Сбер", "ВТБ", "Росбанк")
one, two, three = 1, 2, 3

print('Доступные банки:')

print(one, ':', bank.namebankOne)
print(two, ':', bank.namebankTwo)
print(three, ':', bank.namebankThree)

print('В каком банке вы хотели бы взять ипотеку?')
myBan = input()

class Bid:
    def __init__(self, bidOne, bidTwo, bidThree):
        self.bidOne = bidOne
        self.bidTwo = bidTwo
        self.bidThree = bidThree

bid = Bid("7.7%", "3.9%", "5.2%")

if myBan == '1':
    print('Вы выбрали', bank.namebankOne, 'процентная ставка: ', bid.bidOne)
elif myBan == '2':
    print('Вы выбрали', bank.namebankTwo, 'процентная ставка: ', bid.bidTwo)
elif myBan == '3':
    print('Вы выбрали', bank.namebankThree, 'процентная ставка: ', bid.bidThree)
else:
    print('Выбранного вами банка не существует')
    
print('Просмотреть предложения оставшихся банков? Y/N')
answer = input()


while answer != 'N':

    print('Доступные банки:')

    print(one, ':', bank.namebankOne)
    print(two, ':', bank.namebankTwo)
    print(three, ':', bank.namebankThree)

    print('В каком банке вы хотели бы взять ипотеку?')
    myBan = input()   

    if myBan == '1':
        print('Вы выбрали', bank.namebankOne, 'процентная ставка: ', bid.bidOne)
    elif myBan == '2':
        print('Вы выбрали', bank.namebankTwo, 'процентная ставка: ', bid.bidTwo)
    elif myBan == '3':
        print('Вы выбрали', bank.namebankThree, 'процентная ставка: ', bid.bidThree)
    else:
        print('Выбранного вами банка не существует')
        
    print('Просмотреть предложения оставшихся банков? Y/N')
    answer = input()
      
def WriterMenInfo():
    myData = [["FirstName", "LastName", "Age", "Bank", "Bid"],
          [men.firsname, men.lastname, men.age, bank.namebankOne, bid.bidOne]]
          
 
    myFile = open('WriterInfoMen1.csv', 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        writer.writerows(myData)
     
    print("Запись прошла успешно!")

def WriterMenInfo2():
    myData = [["FirstName", "LastName", "Age", "Bank", "Bid"],
          [men.firsname, men.lastname, men.age, bank.namebankTwo, bid.bidTwo]]
          
 
    myFile = open('WriterInfoMen2.csv', 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        writer.writerows(myData)
     
    print("Запись прошла успешно!")

def DictWriterMenInfo():
    with open('DictWriterMenInfo.csv', 'w') as csvfile:
        fieldnames = ['FirstName', 'LastName', 'Age', 'Bank', 'Bid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
        writer.writeheader()
        writer.writerow({'FirstName': men.firsname, 'LastName': men.lastname, 'Age': men.age, 'Bank': bank.namebankThree, 'Bid': bid.bidThree})
       
    print("Запись прошла успешно!")

if answer == 'N':
    
    print('Поздравляем с выбором банка!')
    if myBan == '1':
        print('Запись Ваших данных с помощью csv.writer  .......')
        WriterMenInfo()

    elif myBan == '2':
        print('Запись Ваших данных с помощью csv.writer  .......')
        WriterMenInfo2()

    elif myBan == '3':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        DictWriterMenInfo()
   

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