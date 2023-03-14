"""
Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python? 


inheritance :
                inheritance is a most powerfull consept in any higher programing  language 
                using of inheritance we can reduse our work 

inheritance
provide reusebulity

using of inheritance we can reduse our work

there are 5 type of inheritance
1)single-level inheovritance
2)multi-level inheritance
3)multiple
4)hybrid 
5)hierachical
"""
class A:
    def input(self):
        self.num1=int(input("Enter the  number 1: "))
        self.num2=int(input("Enter the  number 2: "))
class B(A):
    def addition(self):
        self.ans=self.num1 + self.num2 

    def display(self):
        print(self.ans)

obj = B()
obj.input()
obj.addition()
obj.display()

"""
=====> What is init? Or What Is A Constructor In Python? 

__init__.py : if we put this file in blank folder it will consider as package.

__init__() : this is a function.

which is similar like constructor

by default it call automatic once object of class create.
"""