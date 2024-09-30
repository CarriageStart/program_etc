
FORMAT_STRING = """<rect x="{}" y="{}" z="{}" fill="{}" />"""
FORMAT_STRING2 = """<rect x="{x}" y="{y}" z="{z}" fill="{t}" />"""


# List Unpackging   : Sequence is important
def function(x, y, z, t):
    print(FORMAT_STRING.format(*(locals().values())))

# Dict Unpackging   : Sequence is not important but name 
def function2(x, z, y, t):
    print(FORMAT_STRING2.format(**locals()))


if __name__=="__main__":
    function(1,2,3,4)
    function2(1,2,3,4)

