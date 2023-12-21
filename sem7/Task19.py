# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)
import datetime
class NamedStr(str):
    """"Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)"""
    def __new__(cls, value, name):
        instance = super().__new__(cls, value, name)
        instance.name = name
        instance.time = datetime.datetime.now()
        return instance
a = NamedStr ('cbvhb', 'vhnj')
print(a.name)
print(a.time)
print(NamedStr.__doc__)
