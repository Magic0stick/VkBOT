import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests## импорт библиотеки запросов
from bs4 import BeautifulSoup as bs## импорт библиотеки для разбора 
from scr import *

def found(b,a): ## фунция поиска
    URL_TEMPLATE = b + a ##переменная запроса
    URL_TEMPLATE = URL_TEMPLATE.replace(" ", "") #очистка от лишних пробелов
    r = requests.get(URL_TEMPLATE) #переменная запроса с сервера
    soup = bs(r.text, "html.parser") #переменная анализа информации
    wikiinfo = soup.find('div', class_="post") #поиск информации и задача переменной
    data = wikiinfo.text
    if len(data) > 4093:
        data = (data[0:4093] + '...')
    return data

def translateen(b,a):
    URL_TEMPLATE = b + a ##переменная запроса
    URL_TEMPLATE = URL_TEMPLATE.replace(" ", "") #очистка от лишних пробелов
    r = requests.get(URL_TEMPLATE) #переменная запроса с сервера
    soup = bs(r.text, "html.parser") #переменная анализа информации
    wikiinfo = soup.find('div', class_="ru_title") #поиск информации и задача переменной
    if data == None:
        data = "Ничего не найдено по вашему запросу"
    data = wikiinfo.text
    if len(data) > 4093:
        data = (data[0:4093] + '...')
    return data

def translatefr(b,a):
    URL_TEMPLATE = b + a ##переменная запроса
    URL_TEMPLATE = URL_TEMPLATE.replace(" ", "") #очистка от лишних пробелов
    r = requests.get(URL_TEMPLATE) #переменная запроса с сервера
    soup = bs(r.text, "html.parser") #переменная анализа информации
    wikiinfo = soup.find("p",class_="truncate") #поиск информации и задача переменной
    if data == None:
        data = "Ничего не найдено по вашему запросу"
    data = wikiinfo.text
    data = data[2:]
    if len(data) > 4093:
        data = (data[0:4093] + '...')
    return data

def write_msg(user_id, message): #функция отправки сообщения
    print(message)
    vk.method('messages.send', {'user_id': user_id, 'message': message,"random_id":vk_api.utils.get_random_id()})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            if request == "стоп":
                break
            request = request.lower()
            
            write_msg(event.user_id,translateen(SlovarEN,request))
            write_msg(event.user_id,translatefr(SlovarFR,request))
            write_msg(event.user_id,found(SlovarRU,request))