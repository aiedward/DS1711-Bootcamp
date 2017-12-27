class People:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return (self.name, self.age, self.salary) == (other.name, other.age, other.salary)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)
    
    def __str__(self):
        return self.name + str(self.age) + str(self.salary)
    

if __name__ == "__main__":
    p1 = People("Tom", "1", 20)
    p2 = People("Zion", "2", 18)
    p3 = People("Adam", "3", 20)
    p4 = People("Alice", "4", 18)
    p5 = People("Tom", "1", 18)
    
    dict = {p1: 'Tom:18:20', p2: "Jerry:15:18", p3: "Tom:1:100", p4: "Jerry:4:18", p5: "Jerry:5:18"}
    for key in dict:
        print (key, 'corresponds to', dict[key])

    print("")        
    p5.age = 6
    p5.name = "Bryant"
    for key in dict:
        print (key, 'corresponds to', dict[key]) # lookup
    
    
    
        
    