class bangunruang:
    def volbalok(self,panjang,lebar,tinggi):
        volume = panjang*lebar*tinggi
        print ("volume nya sebesar", volume)
    def selbalok(self,p,l,t):
        ls= 2*((p*l)+(p*t)+(l*t))
        return ls
    def volkerucut(self,jari,tinggi):
        volume = (1/3)*3.14*jari*jari*tinggi
        return volume
    def lkerucut(self,r,s):
        luas=3.14*r*(r+s)
        print('Luas permukaan: ',luas)
    def voltabung(self,jari,tinggi):
        volume=3.14*jari*jari*tinggi
        print ("volume nya sebesar", volume)
    def ltabung(self,r,t):
        luas= 2*3.14*r*(r+t)
        print('Luas permukaan: ',luas)

    def volbola(self,jari):
        volume= 4/3 * 3.14 *jari*jari*jari
        return volume
    def lbola (self,r):
        luas= 4*3.14*r*r
        print('Luas permukaan: ', luas)

a=bangunruang()

def balok():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    p = float(input("masukkan panjang: "))
    l = float(input ("masukkan lebar: "))
    t = float(input ("masukkan tinggi: "))
    
    if (pil==1):
        volume = p*l*t
        print ("volume nya sebesar", volume)
    elif (pil==2):
         ls= 2*((p*l)+(p*t)+(l*t))
         print('Luas selimutnya ', ls)
def kerucut():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    r = float(input("masukkan jari-jari: "))
    t = float(input ("masukkan tinggi: "))
    if (pil==1):
        volume = (1/3)*3.14*r*r*t
        print('volumenya sebesar ',volume)
    elif (pil==2):
        s=float(input('masukkan garis pelukis: '))
        luas=3.14*r*(r+s)
        print("luas permukaan kerucut= ", luas)

def tabung():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas permukaan\nPilihan: '))
    r = float(input("masukkan jari-jari: "))
    t = float(input ("masukkan tinggi: "))
    if (pil==1):
        volume=3.14*r*r*t
        print ("volume tabung= ",volume)
    elif (pil==2):
        luas= 2*3.14*r*(r+t)
        print('Luas permukaan: ',luas)


def bola():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    r = float(input("masukkan jari-jari: "))
    if (pil==1):
        volume= 4/3 * 3.14 *r*r*r
        print('volumenya adalah', volume)
    elif (pil==2):
        luas= 4*3.14*r*r
        print('Luas permukaan: ', luas)
