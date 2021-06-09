


class Human:
default_name = 'no name'
default_age = 2

def__init__(self,name=default_name, age=default_age):
 #Публичные поля
 #Динамичные поля
 self.name = name
 self.age = age
 #приватные поля
 self.__money = 0
 self.__house = None


 def info(self):
     print(f'Name: {self.name}')
     print('Age:{self.age}')
     print('Hiuse{self.house}')
     pr ()





#стат поля
@staticment
def default_info():
    print ('Имя по умолчанию {Human.default_name}')
    print (f'Возраст по умолчанию {Human._default_age}')


    if__name__=="__main__":
        Adina = Human ("Adina",25)
        Adina.info()
        Adina.default_info()



