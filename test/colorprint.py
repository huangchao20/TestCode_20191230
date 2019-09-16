# print('\033[0;36m爆竹声中一岁除，')
# print('春风送暖入屠苏。')
# print('千门万户曈曈日，')
# print('总把新桃换旧符。\033[0m')

# class A:
#     def func(self):
#         print("This is a new Window")
#
# class B(A):
#     def func(self):
#         super().func()
#         print("this is B")
#
# if __name__ == "__main__":
#     A().func()
#     B().func()

# class Base:
#     def __init__( self ):
#         print( "Base.__init__" )
#
# class A(Base):
#     def __init__(self):
#         # super().__init__()
#         Base.__init__(self)
#         print("A.__init__")
#
# class B(Base):
#     def __init__(self):
#         # super().__init__()
#         Base.__init__(self)
#         print("B.__init__")
#
# class C(A, B):
#     def __init__(self):
#         # super().__init__()
#         A.__init__(self)
#         B.__init__(self)
#         print("C.__init__")
#
# C()
# print(C.mro())

class Base:
    def __init__( self ):
        print( "Base.__init__" )

class A(Base):
    def __init__(self):
        super().__init__()
        print("A.__init__")

class B(Base):
    def __init__(self):
        super().__init__()
        print("B.__init__")

class C(A, B):
    def __init__(self):
        print(super())
        super().__init__()
        print("C.__init__")

        print("*" * 100 )

C()
print(C.mro())