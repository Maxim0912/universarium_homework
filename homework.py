import vk_api
import facebook


message = input('Введите Ваше сообщение: ')
while len(message) > 140:
    print(f'Сообщение содержит {len(message)} символов.Не более 140 разрешено')
    message = input('Введите Ваше сообщение: ')

login = input('Введите Ваш логин: ')
password = input('Введите Ваш пароль: ')

try:
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    print(vk.wall.post(message=message))
    print('Сообщение опубликовано успешно.')
except Exception:
    print('Что-то пошло не так. Сообщение не опубликовано.')

facebook_token = input('Введите Ваш facebook token: ')

try:
    graph = facebook.GraphAPI(access_token=facebook_token)
    graph.put_object('me', 'feed', message=message)
    print('Сообщение опубликовано успешно.')
except Exception:
    print('Что-то пошло не так. Сообщение не опубликовано.')
