
class Men:
    def __init__(self, firsname, lastname, age):
        self.firsname = firsname
        self.lastname = lastname
        self.age = age

class Bank:
   def __init__(self, name, bid):
       self.name = name
       self.bid = bid


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
   exit(0)