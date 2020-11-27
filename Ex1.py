age=abs(int(input('Сколько Вам лет? ')))
def prof(age):
    if  0 <= age <= 6:
        return'Учитесь в садике'
    elif 7 <= age <= 17:
        return'Учитесь в школе'
    elif 17 <= age <= 23:
        return'Учитесь в вузе'
    elif 24 <= age <= 60:
        return'Работаете'
    elif 61 <= age <= 100:
        return'Да здравствует пенсия!'

result_age=prof(age) ;      
print(result_age)       