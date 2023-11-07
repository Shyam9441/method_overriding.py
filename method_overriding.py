class employee:
    __sal__ = 20000
    def sal(self)->float:
        return self.__sal__*12

class ContractEmployee(employee):
    __hrpay__: int = 1000
    __hr__= 100
    def sal(self)->float:
         return self.__hrpay__ * self.__hr__

emp=employee()
print(emp.sal())

#method overriding
class Employee :
    __amt = 25000
    def sal(self)-> float:
        return self.__amt * 12
class ContractEmployee(Employee):
     __hrpay = 1000
     __hrs = 10
     def sal(self)-> float:
            return self.__hrpay * self.__hrs
emp = Employee()
print(emp.sal())
