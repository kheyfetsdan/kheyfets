import requests
import json


#Опредилим url тестируемого API
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

#Заголовки всегда используем одинаковые
#Использую 'postman-token' потому что без него почему то пишет, что невалидный ключ апи
headers = {
    'cache-control': "no-cache",
    'postman-token': "b1cf028b-900c-bdd0-468b-808a0031240f"
    }

#Объявим словарь с результатами тестов
test_dict = {}
l = []

#Функция для проверки результа теста
#Передается ожидаемый результат, происходит проверка его совпадения
#Возвращается результат теста
def test_status (expected):
	if parsed_string["status"] == expected:
		test_result = "passed"
	else:
		test_result = "failure"
	return test_result


#Функция сохранения результатов теста
#По ключу (номер теста) записывается лист с результатами, возвращается list 
def test_summary(p_string, test_expected):
	l.append(response.status_code)
	l.append(parsed_string["status"])
	l.append(test_status(test_expected))
	return l

#Переменная для подсчета количества тестов
test_num = 1

#Тест1. 
#key: отправка существующего ключа

#Параметры запроса
querystring = {"location":"55.756961,37.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

#переменная в которую записывается json в формате словаря, для дальнейшего парсинга
parsed_string = json.loads(response.text)

#Запись в словарь результатов теста
test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'OK'))

#После каждого теста отчищаю лист
l.clear()

#Дальнейшие тесты сделаны по аналогии с первым тестом. Где есть отличия описано в комментах (Тест 16 и 17)

#Тест2. 
#key: отправка не существующего ключа

test_num += 1 

querystring = {"location":"55.756961,37.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9Nmy","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'REQUEST_DENIED'))

l.clear()

#Тест3. 
#Проверка валидных координат

test_num += 1 

querystring = {"location":"55.756961,37.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'OK'))

l.clear()

#Тест4. 
#Проверка координат места, которого нет на сервере гугла, но координаты из валидного диапазона (Код 200, "status" : "ZERO_RESULTS")

test_num += 1 

querystring = {"location":"1.756961,37.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'ZERO_RESULTS'))

l.clear()

#Тест5. 
#Проверка несуществующих координат. Первая координата за пределами диапазона

test_num += 1 

querystring = {"location":"-555.756961,37.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест6. 
#Проверка несуществующих координат. Вторая координата за пределами диапазона

test_num += 1 

querystring = {"location":"55.756961,370.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест7. 
#Проверка несуществующих координат. Обе координаты за пределами диапазона

test_num += 1 

querystring = {"location":"555.756961,370.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест8. 
#Проверка несуществующих координат. Одна координата отсутствует

test_num += 1 

querystring = {"location":"55.756961,","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест9. 
#Проверка несуществующих координат. Координаты не числа

test_num += 1 

querystring = {"location":"w,ф","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест10. 
#Проверить одновременное использование параметров radius и rankby=distance

test_num += 1 

querystring = {"location":"55.756961,370.614228","radius":"50","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0", "rankby":"distance"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест11. 
#Проверить граничные значения radius.

test_num += 1 

#В данном тесте я ожидаю "INVALID_REQUEST", но возвращается ZERO_RESULTS либо OK, что противоречит документации
querystring = {"location":"55.756961,37.614228","radius":"50000000","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))
l.clear()

#Тест12. 
#Проверить граничные значения radius.

test_num += 1 

querystring = {"location":"55.756961,370.614228","radius":"-1","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест13. 
#Проверить, что изменение порядка следования параметров не влияет на ответ сервера.

test_num += 1 

querystring = {"key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","radius":"500","maxprice":"4","minprice":"0","location":"55.756961,37.614228"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'OK'))

l.clear()

#Тест14. 
#При отсутствии обязательного параметра возвращается код 200 и статус "status" : "INVALID_REQUEST" (Кроме key)

test_num += 1 

querystring = {"location":"55.756961,370.614228","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'INVALID_REQUEST'))

l.clear()

#Тест15. 
#Ввести все возможные параметры с валидными значениями. Запрос вернет ответ с данными, если они найдены.

test_num += 1 

querystring = {"location":"55.756961,37.614228","radius":"500","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0","language":"ru","type":"bar","keyword":"bar","opennow":"false"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'ZERO_RESULTS'))
l.clear()

#Тест16. 
#Указать параметр language=ru и передать координаты объекта находящегося в России. Запрос вернул информацию на русском языке.

test_num += 1 

querystring = {"location":"55.756961,37.614228","radius":"500","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0","language":"ru"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

#Дополнительная проверка, на наличие кириллицы в ответе, немного костыльно, но смысл понятен
if [s for s in parsed_string["results"][0]["vicinity"] if s in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']: 
	test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'OK'))
else:
	test_dict["Test " + str(test_num)] = "failure"

l.clear()
#Тест17. 
#При введенных minprice=0&maxprice=4 в поисковой выдаче только объекты с определенным price_level

test_num += 1 

querystring = {"location":"55.756961,37.614228","radius":"500","key":"AIzaSyCWOSz0D-dfNnfv7FJh6pP3dghHM9NmyuQ","maxprice":"4","minprice":"0"}
response = requests.request("GET", url,  headers=headers, params=querystring)

parsed_string = json.loads(response.text)

#Дополнительная проверка, на наличие price_level в ответе, по аналогии с тестом на кириллицу
if [s for s in str(parsed_string["results"][0]["price_level"]) if s in '01234']: 
	test_dict["Test " + str(test_num)] = str(test_summary(parsed_string, 'OK'))
else:
	test_dict["Test " + str(test_num)] = "failure"

l.clear()

#Вывод результатов теста на экран
i = 1
while i <= test_num:
    print(test_dict['Test ' + str(i)])
    i = i + 1


