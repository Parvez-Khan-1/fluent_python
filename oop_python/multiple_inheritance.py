
class A:
    def hello(self):
        print("Hello Class A")


class B:
    def hello(self):
        print("Hello Class B")


class C(A, B):
    def hello(self):
        super().hello()


c = C()
c.hello()  # The python Method Resolution Order calls the hello function of Class A

# If we want to call hello func of class B we can call it as below:
# class C(A, B):
#     def hello(self):
#         B.hello(self)
