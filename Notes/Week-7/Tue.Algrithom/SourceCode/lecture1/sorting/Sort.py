# A simple ascending sort is very easy -- just call the sorted() function. It returns a new sorted list:
print(sorted([5, 2, 3, 1, 4]))

# list.sort() method of a list. 
# It modifies the list in-place (and returns None to avoid confusion). 
# Usually it's less convenient than sorted()
a = [5, 2, 3, 1, 4]
a.sort()
print(a)

# Another difference is that the list.sort() method is only defined for lists. 
# In contrast, the sorted() function accepts any iterable.
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

# KEY FUNCTIONS
# Starting with Python 2.4, both list.sort() and sorted() added a key parameter to specify a function 
# to be called on each list element prior to making comparisons.
print(sorted("This is a test string from Kevin".split(), key=str.lower))

# The value of the key parameter should be a function that takes a single argument
# and returns a key to use for sorting purposes. 
# This technique is fast because the key function is called exactly once for each input record.


# LAMDA
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ('Adam', 'A', 10),
]
print( sorted(student_tuples, key=lambda student: student[1]) )

# The same technique works for objects with named attributes
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
# sort by age
print(sorted(student_objects, key=lambda student: student.age))



# Operator Module Functions
from operator import itemgetter, attrgetter, methodcaller

print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))

print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

print([(student.name, student.weighted_grade()) for student in student_objects])
print(sorted(student_objects, key=methodcaller('weighted_grade')))

# Ascending and Descending
print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print(sorted(student_objects, key=attrgetter('age'), reverse=True))


# The Old Way Using the cmp Parameter
# Python 2
#def numeric_compare(x, y):
#    return x - y
#print(sorted([5, 2, 4, 1, 3], cmp=numeric_compare))

# Python 3
def reverse_numeric(x, y):
    return y - x
    
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

print(sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric)))
