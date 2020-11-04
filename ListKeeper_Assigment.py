#Assigment 1
#Start new python file for the module
#define a class ListKeeper with the following properties and API:
#Listkeeper strores named lists (hint: use dictionaries)
#it initializes with a list named example: [1,2,3,4,5]
#    1.show() returns all list names
#    2.add(name, list) adds a new list
#    3.delete(name) deletes list
#    4.sort(name) returns the sorted list name
#    5.append(name, list) appends list to name
#add comments and documentation to your class
#Import your module in this notebook
#write tests to check the functionality of your class

#Solution:

class ListKeeper:
    mydict = {}

    def __init__(self): #Defining initial values example
        self.values = [1, 2, 3, 4, 5]
        self.name = "example"
        ListKeeper.mydict[self.name] = self.values
        #print(ListKeeper.mydict)

    def show(self): #Showing all the list names
        for self.key in ListKeeper.mydict:
            print(self.key)

    def add (self, name, list): #Adding to the dictionary
        ListKeeper.mydict[name]=list
        print(ListKeeper.mydict)

    def delete(self,name): #Deleting from the dictionary
        ListKeeper.mydict.pop(name)
        print(ListKeeper.mydict)

    def sort(self): #sorting the dictionary by names
        for self.key in sorted(ListKeeper.mydict):
            print(self.key)

    def append(self,name,list): #appending the lists to list name
        ListKeeper.mydict[name].append(list)
        print(ListKeeper.mydict)


x= ListKeeper() #creating an instance
#calling functions
x.add("amit",[23])
x.add("john", "California")
x.append("amit",[6,7,8])
x.show()
x.sort()
