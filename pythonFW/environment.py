import os


class Environment:

    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: "http://localhost:8080/library_dev/",
        PROD: "http://localhost:8080/library/"
    }

    def __init__(self):
        self.name = self._get_environment_var()


    @classmethod
    def _get_environment_var(cls):
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            #No variable is set, using default ENVIRONMENT: dev
            return cls.DEV

    def base_url(self):
        return self.URLS[self.name]


ENV = Environment()