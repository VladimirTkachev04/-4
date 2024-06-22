class Users:

    def __init__(self):
        self.userlist = {}

    def add_user(self, username: str, email: str):
        self.userlist[username] = email
        print (f'Данные о пользователе {username} успешно внесены в базу данных')

    def get_email(self, username: str):
        email = self.userlist.get(username, None)
        return email
    
    def get_username(self, email) -> str | None:
        for key, value in self.userlist.items():
            if value == email:
                return key
        
        return None

class Email_sender:
    
    def send_email(self, users: Users, username: str):
        email = users.get_email(username)
        if email:
            print(f'Письмо отправлено пользователю {username} на почту {email}')
        else:
            print(f"Пользователя {username} не существует")


class Report_generator:  

    def generate(self, users: Users, email: str):
        username = users.get_username(email)
        if username:
            print(f'Письмо с отчётом отправлено пользователю {username}')
        else:
            print(f"Пользователя с такой почтой не существует")


users = Users()
users.add_user("Даниил","danil2005@gmail.com")
users.add_user('Виталий',"Vitaly1998@yandex.ru")

sender = Email_sender()
sender.send_email(users, "Даниил")
sender.send_email(users, "Виталий")

reporter = Report_generator()
reporter.generate(users, "danil2005@gmail.com")

print (users.userlist)