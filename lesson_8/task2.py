"""
реализовать метакласс. позволяющий создавать всегда один и тот же объект класса
"""


class DocMeta(type):
    a_class = None

    def __new__(cls, name, bases, dct):
        print(cls, name, bases, dct)
        return type.__new__(cls, name, bases, dct)

    def __call__(self, *args, **kwargs):
        if not self.a_class:
            self.a_class = type.__call__(self, *args, **kwargs)
        return self.a_class


class MyClass(metaclass=DocMeta):
    pass


m_0 = MyClass()
m_1 = MyClass()
m_2 = MyClass()
m_3 = MyClass()
print(m_0 is m_3)  # return True