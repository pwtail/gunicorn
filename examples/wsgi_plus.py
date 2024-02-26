import time
from concurrent.futures import Future
from threading import Thread


def application(environ, start_response):
    def thread():
        time.sleep(3)
        fut.set_result(3)

    Thread(target=thread).start()
    fut = Future()
    yield fut
    body = b'Dzozdra!\n'
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    yield body
