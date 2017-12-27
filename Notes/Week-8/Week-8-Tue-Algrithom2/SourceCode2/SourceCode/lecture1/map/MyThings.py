from collections import namedtuple

MyThingBase = namedtuple("MyThingBase", ["name", "location"])
class MyThing(MyThingBase):
    def __new__(cls, name, location, length):
        obj = MyThingBase.__new__(cls, name, location)
        obj.length = length
        return obj

a = MyThing("a", "here", 10)
b = MyThing("a", "here", 20)
c = MyThing("c", "there", 30)
print(a == b)
# True
print(hash(a) == hash(b))
# True
print(a == c)
# False


dict = {a: a.length, b: b.length, c: c.length}
for key in dict:
    print (key, 'corresponds to', dict[key])
    
a.length = 100
for key in dict:
    print (key, 'corresponds to', dict[key])
    
a.name = "xyz"
#for key in dict:
#    print (key, 'corresponds to', dict[key])

