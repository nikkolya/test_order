import requests
import socket

url  = "http://"+str(socket.gethostbyname (socket.getfqdn())) + ":5000"

def test_put():
    try:
        js = {
            "text" : "Тестовый текст!",
            "rubrics" : ["Раз","Два"]
        }
        put = requests.put(url = url + "/put/text", json=js)
        print(put.text)
        return put.json()['body']['id']
    except:
        print("Error in put method")
def test_get():
    try:
        js = {
            "text" : "Тест"
        }
        put = requests.get(url = url + "/get/text", json=js)
        print(put.text)
    except:
        print("Error in get method")
def test_del(id):
    try:
        js = {
            "id" : id
        }
        put = requests.delete(url = url + "/del/text", json=js)
        print(put.text)
    except:
        print("Error in del method")
print("----------\nМетод PUT")
ret_id =test_put()
print("----------\nМетод GET")
test_get()
print("----------\nМетод DEL")
test_del(ret_id)
print("----------")