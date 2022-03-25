class A:

    def __init__(self,*args):

        self.args = args
    def __str__(self):
        return f"{self.args}"




obj = A(1)
obj1 = A(12,2,3)

print(obj)
print(obj1)