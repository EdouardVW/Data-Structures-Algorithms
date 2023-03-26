class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

cookie1 = Cookie('green')
cookie2 = Cookie('blue')

print(f'Cookie one is {cookie1.get_color()}')
print(f'Cookie two is {cookie2.get_color()}')

cookie1.set_color('orange')

print(f'Cookie one is now {cookie1.get_color()}')
print(f'Cookie two is still {cookie2.get_color()}')


###################################


class LinkedList:
    def __init__(self,value):
        pass

    def append(self, value):
        pass

    def pop(self):
        pass

    def prepend(self,value):
        pass

    def insert(self,index,value):
        pass

    def remove(self,index):
        pass

