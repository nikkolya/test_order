from aiohttp import web
import json
from DB.main_db import DB
import emoji
import datetime


class Aio_app:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = web.Application()
        self.db = DB()

    async def get_text(self, request):
        try:
            params = await request.json()
            text = emoji.demojize(params['text'])
            results = self.db.get_text(text)
            mass = []
            if range(len(results)) == 0:
                return web.HTTPBadRequest(text=json.dumps({'status': 'error', 'body': "No rows"}))
            for i in range(len(results)):
                cort = {
                    "id": results[i][0],
                    "rubrics": results[i][1].split(','),
                    "text": results[i][2],
                    "created_date": results[i][3]
                }
                mass.append(cort)
            js = {
                "status": "success",
                "body": mass
            }
            return web.json_response(js)
        except Exception as error:
            return web.HTTPBadRequest(text=json.dumps({'status': 'error', 'body': str(error)}))

    async def put_text(self, request):
        try:
            params = await request.json()
            rubrics = params["rubrics"]
            text = emoji.demojize(params["text"])
            try:
                created_date = datetime.datetime.strptime(params["created_date"], "%Y-%m-%d %H:%M:%S")
                created_date = created_date.strftime("%d.%m.%Y %H:%M:%S")
            except:
                created_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            result = self.db.put_text(rubrics=rubrics, text=text, created_date=created_date)
            js = {
                "status": "success",
                "body": {
                    "id": result
                }
            }
            return web.json_response(js)
        except Exception as error:
            return web.HTTPBadRequest(text=json.dumps({'status': 'error', 'body': str(error)}))

    async def del_text(self, request):
        try:
            params = await request.json()
            row_ID = params["id"]
            result = self.db.del_text(row_ID)
            if result == 1:
                js = {
                    "status": "success",
                    "body": {
                        "deleted": True
                    }
                }
                return web.json_response(js)
            else:
                return web.HTTPBadRequest(text=json.dumps({'status': 'error', 'body': 'No rows for delete'}))
        except Exception as error:
            return web.HTTPBadRequest(text=json.dumps({'status': 'error', 'body': str(error)}))

    def start_app(self):
        self.app.router.add_route('GET', '/get/text', self.get_text)
        self.app.router.add_route('PUT', '/put/text', self.put_text)
        self.app.router.add_route('DELETE', '/del/text', self.del_text)

        web.run_app(self.app, host=self.host, port=self.port)
