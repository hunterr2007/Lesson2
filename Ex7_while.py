asks={"Привет!": "Привет, бро!", "Как дела?": "Всё отлично!", "Что делаешь?": "Программирую"}
def ask_user(question):
    while asks.get(question)!=None:
            w = asks.get(question)
            print(w)
            break 
    else:
        print('Что?')
        ask_user(input())      
ask_user(input())      
