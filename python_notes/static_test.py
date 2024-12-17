
class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self, delta=1):
        self.value += delta

    def decrement(self, delta=1):
        self.value -= delta

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    # Like "self" key word, "cls" keyword is conventionally used as first parameter name
    #   The first parameter of class methods is always the class name
    @classmethod    
    def fromTuple(cls, tup):    # Factory method
        return cls(tup[0], tup[1])

    @classmethod
    def fromDictionary(cls, dic):
        return cls(dic["email"], dic["password"])

    # This also acts like class method, but class name is not inserted as a first parameter.
    def test(x):
        print(type(x))

class StringUtils:
    #  Static decorator is necessary to make method static, 
    # since the object is implicitly inserted as a first parameter.
    @staticmethod
    def toCamelcase(text):
        words = iter(text.split("_"))
        return next(words) + "".join(i.title() for i in words) # Generator comprehension

    @staticmethod
    def toSnakecase(text):
        letteres = ["_" + i.lower() if i.isupper() else i for i in text]
        return "".join(letteres).lstrip("_")


if __name__=="__main__" :
    # Method
    counter = Counter()
    counter.decrement()

    # Class method
    user = User.fromTuple(("user@test.com", "1234"))

    # Static method
    StringUtils.toCamelcase("last_modified_date")
    




