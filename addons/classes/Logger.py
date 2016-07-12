class Logger(object):
    def logerror(self, arg):
        with open('logs/error.log', 'a') as errorlog:
            errorlog.write(arg)
        print 'error logged'

    def logaccess(self, arg):
        with open('logs/access.log', 'a') as accesslog:
            accesslog.write(arg)
        print 'access logged'
