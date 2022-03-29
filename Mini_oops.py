class StringClass:
    def __init__(self, demo):
        self.demo = demo
    def lis(self):
        return(list(self.demo))
    def len(self):
        return len(self.demo)
class PairsPossible(StringClass):
    def pair(self,test_list):
        res = [(a , b) for i, a in enumerate(test_list) for b in test_list[i + 1:]]
        print(res)
a = input()
b = StringClass(a)
print(b.lis())
print(b.len())
c = b.lis()
d = PairsPossible(b)
d.pair(c)
