def hello_user(ask_qwestion):
    while True:
        if ask_qwestion == 'Хорошо':
            print('Рад за тебя!')
            break
        else:
            hello_user(input('Как дела? '))

hello_user(input('Как дела? '))
