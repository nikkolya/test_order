from API import api_app

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app = api_app.Aio_app(host = host,
                          port =  port)
    app.start_app()