import csv
import socket
import requests
import datetime

def insert_test_csv(obj):
    reader = csv.DictReader(obj, delimiter=',')
    rows = list(reader)
    len_rows = len(rows)
    i = 1
    for i, row in enumerate(rows):
        text = str(row["text"])
        created_date = datetime.datetime.strptime(row["created_date"],"%Y-%m-%d %H:%M:%S")
        rubrics = row["rubrics"].replace('[','').replace(']','').replace("'",'').replace(" ",'').split(",")
        js = {
            "text":text,
            "created_date":str(created_date),
            "rubrics":rubrics
        }
        insert = requests.put(url+"/put/text",json=js)
        print(insert.text)
        print("Completed {0} out of {1}".format(i+1,len_rows))
        i +=1
    print("Done")


if __name__ == "__main__":
    url  = "http://"+str(socket.gethostbyname (socket.getfqdn())) + ":5000" #Т.к. сервер локальный и запущен на 0.0.0.0, то получим присвоенный машине IP и добавим порт выбранный по умолчанию -- 5000
    with open("posts.csv", "r", encoding='utf-8') as obj:
        insert_test_csv(obj)