#abstract method has only declaration and not have definition
#python default does not support abstract class
#we cann't create object
#ABC - Abstract Base Class
#And also we cann't inherit the subclass buy using abstract class
#we defind that method means we can access that 
from abc import ABC,abstractmethod


class computer(ABC):
    @abstractmethod
    def process():
        pass
class laptop(computer):
    def process(self):
        print("it working now")




#com = computer()
#com.process()
com1=laptop()
com1.process()

from abc import ABC,abstractmethod

class employee_name(ABC):
    @abstractmethod
    def info():
        pass
class employee_id():
    def detail(self):
        print("it process")

obj = employee_id()
obj.detail()
