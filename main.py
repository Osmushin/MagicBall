from random import *

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть в этом уверен',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока не ясно, пробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как вас зовут?')
name = input()
print('Приветствую тебя,', name, '!')


def magic_ball():
    print('Какой вопрос вы хотите задать?')
    input()
    print(choice(answers))
    print('У вас есть еще вопросы? Если хотите задать вопрос напишите "да", если вопросов не осталось напишите "нет"')
    if input().lower() == 'да':
        return True
    else:
        print('Возвращайся если возникнут вопросы!')


while magic_ball() == True:
    magic_ball()