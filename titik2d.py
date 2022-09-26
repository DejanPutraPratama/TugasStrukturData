class DuaDimensi:
  x = 0
  y = 0

  def __init__(self,x,y):
    self.x = x
    self.y = y
  def geserHorizontal(self,dx):
    self.x += dx
  def geserVertikal(self,dy):
    self.y += dy
  def hitungJarak(self, titikLain):
    jarak_x = titikLain.getX() - self.getX()
    jarak_y = titikLain.getY() - self.getY()
    jarak = (jarak_x**2 + jarak_y**2)**0.5
    return jarak 
  def getX(self):
    return self.x
  def getY(self):
    return self.y
        
t1 = DuaDimensi(2,3)  
t2 = DuaDimensi(4,5) 

t1.geserHorizontal(-3)
t1.geserVertikal(-7)
print("Koordinat titik t1 = ", (t1.getX(), t1.getY()))

t2.geserHorizontal(15)
t2.geserVertikal(9)
print("Koordinat titik t2 = ", (t2.getX(), t2.getY()))

print(t1.hitungJarak(t2))



