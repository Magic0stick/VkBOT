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
    answer = "нет информации"
    info = ""
    for info in wikiinfo: #цикл поиска текста(нужен при множественных ответах)
        answer = info.text
    answer = answer.replace("''","")
    print(answer)
    if answer == "":
        answer = "нет информации"
    write_msg(event.user_id, answer)

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
            
            request = request.lower()
            print(request)
            
            print("run answer")
            found(SlovarRU,request)
            found(SlovarEN,request)
            found(SlovarFR,request)
            print("end answer")