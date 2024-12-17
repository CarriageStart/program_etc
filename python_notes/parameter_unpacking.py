import functools

FORMAT_STRING = """<rect x="{}" y="{}" z="{}" fill="{}" />"""
FORMAT_STRING2 = """<rect x="{x}" y="{y}" z="{z}" fill="{t}" />"""


# List Unpackging   : Sequence is important
def function(x, y, z, t):
    print(FORMAT_STRING.format(*(locals().values())))

# Dict Unpackging   : Sequence is not important but name 
def function2(x, z, y, t):
    print(FORMAT_STRING2.format(**locals()))

# If you don't know how many parameters are, like decorator
def do_twice(function): # Arbitrary function
    @functools.wraps(function)  # Update defined function's metadata to fucion's
    def wrapper_do_twice(*args, **kwargs):  # No one knows how many parameter will given
        function(*args, **kwargs)
        return function(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def sayHello(name, name2):
    print(f"{name} says 'Hello' to {name2}")


if __name__=="__main__":
    function(1,2,3,4)
    function2(1,2,3,4)
    sayHello("Kihoon", "Sujin")

