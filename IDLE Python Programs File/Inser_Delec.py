class insertion:
    def getdata(self, array,position,value,size):
        self.ar = array
        self.po = position
        self.va = value
        self.s = size

class insert_cal(insertion):
    def cal(self):
        a = self.ar
        pos = self.po
        val = self.va
        n = self.s

        for i in range(n-1, pos-1, -1):
            a[i+1] = a[i]
        a[pos] = val

        for i in range(0, n+1):
            print('\n ',a[i])

class deletion:
    def getdata1(self, arr, position1, size1):
        self.myar = arr
        self.posi = position1
        self.n2 = size1

class delet_cal(deletion):
    def cal2(self):
        b = self.myar
        pos1 = self.posi
        n1 = self.n2

        for k in range(pos1, n1):
            b[k] = b[k+1]

        for k in range(0, n1-1):
            print(' \n ',b[k])

obj = insert_cal()
obj1 = delet_cal()

print(" Insertion ")
obj.getdata([12,34,23,41,14],2,45,4)
obj.cal()

print(' \n ')

print(" Deletion ")
obj1.getdata1([34,23,4,12,14],3,4)
obj1.cal2()
            
            
        
