class User:
    name: str
    secondname: str
    email: str

    def __init__(self, name, secondname, email):
        self.name = name
        self.secondName = secondname
        self.email = email

    @staticmethod
    def userinfo(name: str, secondname: str, email: str):
        return {
            "name": name,
            "secondname": secondname,
            "email": email
        }



