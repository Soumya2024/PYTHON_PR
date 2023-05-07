class Sorting:
    def B_sort(self, arr,size):
        self.arr2 = arr
        self.size2 = size
    def S_sort(self1, arr1,size1):
        self1.arr12 = arr1
        self1.size12 = size1

class Bubble(Sorting):
    def cal(self):
        k = self.arr2
        l = self.size2

        for i in range(0, l):
            for j in range(i+1, l):
                if k[i]>k[j]:
                    temp = k[j]
                    k[j] = k[i]
                    k[i] = temp

        for i in range(0,l):
            print(k[i])

class Selection(Sorting):
    def cal1(self1):
        g = self1.arr12
        d = self1.size12

        for s in range(0,d):
            min = s
            for f in range(s, d):
                if g[min]<g[f]:
                    min = f
            #if min>s:
                temp1 = g[s]
                g[s] = g[min]
                g[min] = temp1

        for s in range(0,d):
            print(g[d])


obj = Bubble()
obj1 = Selection()


obj.B_sort([3,2,5,1,6,8,5],6)
obj.cal()

print(' \n ')

obj1.S_sort([3,5,4,1,7,6,9,3],7)
obj1.cal1()
                
