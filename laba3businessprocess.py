
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

if answer == 'N':
 
   print('Поздравляем с выбором банка!')
   exit(0)