def getrespondcode(request):
    if ('GET / HTTP/1.1' or 'GET /index.html HTTP/1.1' or 'GET / HTTP/1.0' or 'GET /index.html HTTP/1.0'
            or 'GET /upload HTTP/1.1' or 'GET /upload.html HTTP/1.1' or 'GET /upload.html HTTP/1.0'
            in request.split('\n')[0]):
        return 'HTTP/1.1 200 OK\n\n'
    else:
        return 'HTTP/1.1 404 Not Found\n\n'
