import time
from threading import Thread


def application(environ, start_response, resume):
    def thread():
        time.sleep(10)
        resume()
    Thread(target=thread).start()
    yield resume
    body = b'Dzozdra!\n'
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    yield body
