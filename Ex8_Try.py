def hello_user(ask_qwestion):
    try:  
        while True:
            if ask_qwestion == 'Хорошо':
                print('Рад за тебя!')
                break
            else:
                hello_user(input('Как дела? '))
    except KeyboardInterrupt:
        print('Пока')   
hello_user(input('Как дела? '))