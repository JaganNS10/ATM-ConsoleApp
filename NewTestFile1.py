class Calculator():
    def __init__(self):
        self.store=[]
        i=0
        while True:
            i=i+1
            UserInput=float(input(f"Enter The Number {i}:"))
            operation=input(f"Enter the Symbol {i}:")
            self.store.append(UserInput)
            self.store.append(operation)
            result="ANSWER"
            res="YES"
            if operation=="=" or operation==result.lower() or operation== result.upper() or operation==result.title():
                Input=input("Are You want To See Your Answer:")
                if Input ==res.lower() or Input==res.upper() or Input==res.title():
                    break
                else:
                    continue
    def display(self):
          self.store.remove(self.store[-1])
          self.sum=self.store[0]
          for i in range(1,len(self.store),2):
              if self.store[i]=="+":
                   self.sum=self.sum+self.store[i+1]
              elif self.store[i]=="-":
                   self.sum=self.sum-self.store[i+1]
              elif self.store[i]=="%":
                  self.sum=self.sum%self.store[i+1]
              elif self.store[i]=="//":
                  self.sum=self.sum//self.store[i+1]
              elif self.store[i]=="*":
                  self.sum=self.sum*self.store[i+1]
          print("Your ans is:",self.sum)

    
object = Calculator()
object.display()








