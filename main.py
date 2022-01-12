#wg=1, wr=2, wb=3, wo=4, gr=5, rb=6, bo=7, og=8, yg=9, yr=10, yb=11, yo=12
#wgr=13, wrb=14, wbo=15, wog=16, ygr=17, yrb=18, ybo=19, yog=20
#orientation is white and green with white on top

class piece:
  def __init__(self, type, piece, x, y, z, orientation):
    self.type = type
    self.x = x
    self.y = y
    self.z = z
    self.orientation = orientation
    self.piece = piece
    self.type = type

wg = piece(True, 1, 2, 3, 1, 1)
wr = piece(True, 2, 3, 3, 2, 1)
wb = piece(True, 3, 2, 3, 3, 1)
wo = piece(True, 4, 1, 3, 2, 1)
gr = piece(True, 5, 3, 2, 1, 1)
rb = piece(True, 6, 3, 2, 3, 1)
bo = piece(True, 7, 1, 2, 3, 1)
og = piece(True, 8, 1, 2, 1, 1)
yg = piece(True, 9, 2, 1, 1, 1)
yr = piece(True, 10, 3, 1, 2, 1)
yb = piece(True, 11, 2, 1, 3, 1)
yo = piece(True, 12, 1, 1, 2, 1)
wgr = piece(False, 13, 3, 3, 1, 1)
wrb = piece(False, 14, 3, 3, 3, 1)
wbo = piece(False, 15, 1, 3, 3, 1)
wog = piece(False, 15, 1, 3, 1, 1)
ygr = piece(False, 17, 3, 1, 1, 1)
yrb = piece(False, 18, 3, 1, 3, 1)
ybo = piece(False, 19, 1, 1, 3, 1)
yog = piece(False, 20, 1, 1, 1, 1)

#R = 1, L = 2, U = 3, D = 4 ,F = 5, B = 6
#normal = 1, prime = 2, twice = 3

def loc(piece):
  return(piece.x, piece.y, piece.z)

def reg(self):
  if self.type == False:
    while self.orientation > 3:
      self.orientation -= 3
  else:
    while self.orientation > 2:
      self.orientation -= 2

def findpiece(x, y, z):
  if x%2 == 1 and y%2 == 1 and z%2 == 1:
    if loc(wgr) == (x, y, z):
      return(wgr)
    if loc(wrb) == (x, y, z):
      return(wrb)
    if loc(wbo) == (x, y, z):
      return(wbo)
    if loc(wog) == (x, y, z):
      return(wog)
    if loc(ygr) == (x, y, z):
      return(ygr)
    if loc(yrb) == (x, y, z):
      return(yrb)
    if loc(ybo) == (x, y, z):
      return(ybo)
    if loc(yog) == (x, y, z):
      return(yog)
  else:
    if y == 3:
      if z == 3:
        return(wb)
      if z == 1:
        return(wg)
      if z == 2:
        if loc(wo) == (x, y, z):
          return(wo)
        else:
          return(wr)
    if y == 1:
      if z == 3:
        return(yb)
      if z == 1:
        return(yg)
      if z == 2:
        if loc(yo) == (x, y, z):
          return(yo)
        else:
          return(yr)
    if y == 2:
      if loc(gr) == (x, y, z):
        return(gr)
      if loc(rb) == (x, y, z):
        return(rb)
      if loc(bo) == (x, y, z):
        return(bo)
      if loc(og) == (x, y, z):
        return(bo)

def R():
#moving corners
  findpiece(3, 1, 1).y += 2
  findpiece(3, 1, 1).orientation += 1
  reg(findpiece(3, 1, 1))
  findpiece(3, 3, 1).z += 2
  findpiece(3, 3, 1).orientation += 2
  reg(findpiece(3, 3, 1))
  findpiece(3, 3, 3).y -= 2
  findpiece(3, 3, 3).orientation += 1
  reg(findpiece(3, 3, 3))
  findpiece(3, 1, 3).z -= 2
  findpiece(3, 1, 3).orientation += 2
  reg(findpiece(3, 1, 3))
#moving edges
  findpiece(3, 2, 1).z += 1
  findpiece(3, 2, 1).y += 1
  findpiece(3, 3, 2).z += 1
  findpiece(3, 3, 2).y -= 1
  findpiece(3, 2, 3).z -= 1
  findpiece(3, 2, 3).y -= 1
  findpiece(3, 1, 2).z -= 1
  findpiece(3, 1, 2).y += 1 

def L():
#moving corners
  findpiece(1, 1, 1).y += 2
  findpiece(1, 1, 1).orientation += 1
  reg(findpiece(1, 1, 1))
  findpiece(1, 3, 1).z += 2
  findpiece(1, 3, 1).orientation += 2
  reg(findpiece(1, 3, 1))
  findpiece(1, 3, 3).y -= 2
  findpiece(1, 3, 3).orientation += 1
  reg(findpiece(1, 3, 3))
  findpiece(1, 1, 3).y -= 2
  findpiece(1, 1, 3).orientation += 2
  reg(findpiece(1, 1, 3))
#moving edges
  findpiece(1, 2, 1).z += 1
  findpiece(1, 2, 1).y += 1
  findpiece(1, 3, 2).z += 1
  findpiece(1, 3, 2).y -= 1
  findpiece(1, 2, 3).z -= 1
  findpiece(1, 2, 3).y -= 1
  findpiece(1, 1, 2).z -= 1
  findpiece(1, 1, 2).y += 1

def U():
#moving corners
  findpiece(3, 3, 1).x -= 2
  findpiece(1, 3, 1).z += 2
  findpiece(1, 3, 3).x += 2
  findpiece(3, 3, 3).z -= 2
#moving edges
  findpiece(2, 3, 1).x -= 1
  findpiece(2, 3, 1).z += 1
  findpiece(1, 3, 2).x += 1
  findpiece(1, 3, 2).z += 1
  findpiece(2, 3, 3).x += 1
  findpiece(2, 3, 3).z -= 1
  findpiece(3, 3, 2).z -= 1
  findpiece(3, 3, 2).x -= 1

def D():
#moving corners
  findpiece(3, 1, 1).z += 2
  findpiece(1, 1, 1).x += 2
  findpiece(1, 1, 3).z -= 2
  findpiece(3, 1, 3).x -= 2
#moving edges
  findpiece(2, 1, 1).x += 1
  findpiece(2, 1, 1).z -= 1
  findpiece(1, 1, 2).x += 1
  findpiece(1, 1, 2).z -= 1
  findpiece(2, 1, 3).x -= 1
  findpiece(2, 1, 3).z += 1
  findpiece(3, 1, 2).z += 1
  findpiece(3, 1, 2).x += 1

def F():
#moving corners
  findpiece(1, 3, 1).x += 2
  findpiece(1, 3, 1).orientation += 1
  reg(findpiece(1, 3, 1))
  findpiece(3, 3, 1).y -= 2
  findpiece(3, 3, 1).orientation += 2
  reg(findpiece(3, 3, 1))
  findpiece(3, 1, 1).x -= 2
  findpiece(3, 1, 1).orientation += 1
  reg(findpiece(3, 1, 1))
  findpiece(1, 1, 1).y += 2
  findpiece(1, 1, 1).orientation += 2
  reg(findpiece(1, 1, 1))
#moving edges
  findpiece(2, 3, 1).x += 1
  findpiece(2, 3, 1).y -= 1
  findpiece(2, 3, 1).orientation
  reg(findpiece(2, 3, 1))
  findpiece(3, 2, 1).x -= 1
  findpiece(3, 2, 1).y -= 1
  findpiece(3, 2, 1).orientation += 1
  reg(findpiece(3, 2, 1))
  findpiece(2, 1, 1).x -= 1
  findpiece(2, 1, 1).y += 1
  findpiece(2, 1, 1).orientation += 1
  reg(findpiece(2, 1, 1))
  findpiece(1, 2, 1).x += 1
  findpiece(1, 2, 1).y += 1
  findpiece(1, 2, 1).orientation += 1
  reg(findpiece(1, 2, 1))

def B():
#moving corners
  findpiece(1, 3, 3).x += 2
  findpiece(1, 3, 3).orientation += 1
  reg(findpiece(1, 3, 3))
  findpiece(3, 3, 3).y -= 2
  findpiece(3, 3, 3).orientation += 2
  reg(findpiece(3, 3, 3))
  findpiece(3, 1, 3).x -= 2
  findpiece(3, 1, 3).orientation += 1
  reg(findpiece(3, 1, 3))
  findpiece(1, 1, 3).y += 2
  findpiece(1, 1, 3).orientation += 2
  reg(findpiece(1, 1, 3))
#moving edges
  findpiece(2, 3, 3).x -= 1
  findpiece(2, 3, 3).y -= 1
  findpiece(2, 3, 3).orientation += 1
  reg(findpiece(2, 3, 3))
  findpiece(1, 2, 3).x += 1
  findpiece(1, 2, 3).y -= 1
  findpiece(1, 2, 3).orientation += 1
  reg(findpiece(1, 2, 3))
  findpiece(2, 1, 3).x += 1
  findpiece(2, 1, 3).y += 1
  findpiece(2, 1, 3).orientation += 1
  reg(findpiece(2, 1, 3))
  findpiece(3, 2, 3).x -= 1
  findpiece(3, 2, 3).y += 1
  findpiece(3, 2, 3).orientation += 1
  reg(findpiece(3, 2, 3))

print("the code kinda worked i guess")