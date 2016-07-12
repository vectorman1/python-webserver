class Content(object):
    def returnindex(self):
        with open('files/index.html') as indexfile:
            index = indexfile.read()
            print('serving index.html')
            return index

    def returnupload(self):
        with open('files/upload.html') as uploadfile:
            upload = uploadfile.read()
            print 'serving upload.html'
            return upload

    def return404(self):
        pass
