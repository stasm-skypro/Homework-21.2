from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за обработку входящих запросов от клиентов.
    """

    def do_GET(self) -> None:
        """Метод для обработки входящих GET-запросов."""

        path = self.get_path_to_html()
        print(path)

        try:
            with open(path, "r", encoding="utf-8") as file:
                page_content = file.read()

        except FileNotFoundError:
            self.send_error(404, "File %s Not Found" % path)

        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_content, "utf-8"))

    def do_POST(self) -> None:
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        response = "Received POST data: %s" % post_data.decode("utf-8")
        print(response)

    def get_path_to_html(self) -> str:
        if self.path == "/":
            return "../html/contacts.html"
        return self.path[1:]


def main() -> None:
    webServer = HTTPServer((hostName, serverPort), MyHTTPRequestHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Запуск веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети, принимать запросы и отправлять их на
    # обработку специальному классу, описанному выше.
    main()
