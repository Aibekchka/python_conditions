# BRANCH TASK 1
month = int(input('Жыл айын енгізіңіз '))
if month >= 1 and month <= 2 or month ==12:
   print("Ай мезгілі Қыс.")
elif month >= 3 and month <= 5:
   print("Ай мезгілі Көктем.")
elif month >= 6 and month <= 8:
   print("Ай мезгілі Жаз.")
elif month >=9 and month <=11:
    print("Ай мезгілі Күз")

# BRANCH TASK 2
age = int(input('Добро пожаловать , Введите возраст: '))
if age >17:
    print('Вы совершеннолетний')
else:
    print('Вы не совершеннолетний')


# < = Кіші
# > = Көп



# BRANCH LOGICAL OPERATORS TASK
milk = not False  # Сүт "бар ЕМЕС".
cereals = True   # Хлопья бар.
eggs = False    # Жұмыртқа жоқ.
if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereals:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"
print("Сегодня на завтрак", breakfast)

# LOGICAL OPERATORS 1
temperature = int(input('Бүгін дала қанша градус ? '))
temperature2 = 26
sun = True
if sun and temperature > 25:
     print('Ауа райы жақсы, серуендеуге болады')
else:
     print('Ауа рай бүгіндікке жаман, үйде кітап оқып отырамыз')


# LOGICAL OPERATORS 2
age = int(input('Жасыңызды енгізіңіз: '))
if age >= 1 and age <= 12:
        print('Балалық шақ')
elif age >=13 and age <= 19:
    print('Мүшел жас, Жастық шақ')
elif age >=20 and age <= 50:
    print('Егде жас')
elif age >= 50 and age <= 60:
    print('Кәрілік')
else:
    print('Зейнеталық жас')


# LOGICAL OPERATORS 3
order_price = int(input('Заказ бағасын енгізіңіз '))
country = input('Сізге қай елге жеткізіп беру керек? ')
if order_price > 10000 and country == 'Canada' or country == 'USA' and  order_price > 10000:
    print('Доставка бесплатная')
elif order_price > 7000 and country == 'Canada' or country == 'USA' and order_price > 7000:
    print('Доставка 10$')
else:
    print('Доставка 20$')


# LOGICAL OPERATORS 4
order_price = int(input('Введите сумму заказа '))
country = input('Введите страну доставки: ')
if order_price > 1000 and (country == 'Canada' or country == 'USA'):
    print('')



# HOME TASK
print('Добро пожаловать в наш магазин одежды')
order_price = int(input('Введите сумму заказа '))
if order_price > 9999:
     print('Цена с учетом скидки',int(order_price-(order_price/10)))
else:
     print('Скидка не доступна')

# HOME TASK 2
print('Добро пожаловать в наш магазин одежды')
order_price = int(input('Введите сумму заказ '))
if order_price > 9999:
    sales_percent = int(input('Введите процент скидки '))
    order_price = order_price -int(order_price * sales_percent/100)
    print('Цена с учетом скидки', order_price)
else:
    print('Скидка не доступна')




for current_hour in range(24):
    if current_hour < 12:
        print('Қайырлы таң')
    else:
        print('Қайырлы күн')


for current_hour in range(0,24):
    print('Сағат '+ str(current_hour) + ":00.")
    if current_hour < 6:
        print('Қайырлы түн!')
    elif current_hour < 12:
        print('Қайырлы таң!')
    elif current_hour < 18:
        print('Қайырлы күн!')
    elif current_hour < 23:
        print('Қайырлы кеш!')
    else:
        print('Қайырлы түн!')







