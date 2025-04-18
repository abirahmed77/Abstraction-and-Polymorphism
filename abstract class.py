from abc import ABC, abstractmethod

class AbsClass(ABC):
    def print(self, x):
        print(f"Passed value : {x}")
        
    @abstractmethod
    def task(self):
        print("We are inside AbsClass taski method")
        
class TestClass(AbsClass):
    def task(self):
        print("We are inside TestClass task method")
        
testObj = TestClass()
testObj.task()
testObj.print(100)
