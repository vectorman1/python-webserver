from addons.classes.Logger import Logger
from addons.classes.Content import Content

content = Content()
logger = Logger()

def getcontent(pathrequested):
    if 'GET / HTTP/1.1' in pathrequested or 'GET /index.html HTTP/1.1' in pathrequested\
            or 'GET / HTTP/1.0' in pathrequested or 'GET /index.html HTTP/1.0' in pathrequested:
        return content.returnindex()

    if 'GET /upload HTTP/1.1' in pathrequested or 'GET /upload.html HTTP/1.1' in pathrequested \
            or 'GET /upload HTTP/1.0' in pathrequested or 'GET /upload.html HTTP/1.0' in pathrequested:
        return content.returnupload()

    content.return404()
    logger.logerror('Unknown Path requested\n')