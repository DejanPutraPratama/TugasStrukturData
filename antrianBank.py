class antrean :
  panggil = 0
  antrean = 0
  def __init__(self, panggil = 0, antrean = 0) :
    self.panggil = panggil
    self.antrean = antrean
  def upPanggil(self):
    if self.panggil == self.antrean:
      return print("No Antrean Belum ada")
    else :
      self.panggil += 1
  def upAntrean(self):
    self.antrean += 1
  def reset(self):
    self.panggil = 0
    self.antrean = 0
  def getPanggil (self):
    return self.panggil
  def getantrean (self):
    return self.antrean
antrean = antrean()
antrean.upAntrean()
antrean.upAntrean()
antrean.upAntrean()
antrean.upPanggil()
antrean.upPanggil()
antrean.upPanggil()
antrean.upPanggil()
antrean.upAntrean()
antrean.upPanggil()

print("No antrean terkini :",antrean.getantrean())
print("No antrean yang dipanggil :",antrean.getPanggil())



