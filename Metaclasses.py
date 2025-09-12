# Example of using metaclasses in Python

# Define a simple metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with MyMeta")
        dct['created_by_metaclass'] = True
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class definition
class MyClass(metaclass=MyMeta):
    pass

# Test the class
if __name__ == "__main__":
    obj = MyClass()
    print(f"created_by_metaclass: {obj.created_by_metaclass}")