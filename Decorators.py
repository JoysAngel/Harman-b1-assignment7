def hello(func):
    print("Execute me First")
    func() #prin
    
@hello
def printname():
    print("Rahul")
