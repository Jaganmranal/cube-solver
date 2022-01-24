#wg=1, wr=2, wb=3, wo=4, gr=5, rb=6, bo=7, og=8, yg=9, yr=10, yb=11, yo=12
#wgr=13, wrb=14, wbo=15, wog=16, ygr=17, yrb=18, ybo=19, yog=20
#orientation is white and green with white on top
#white=1, yellow=2, green=3, blue=4, red=5, orange=6

import copy

class piece:
  def __init__(self, piece, identity, x, y, z, orientation, key, partner1, partner2):
    self.piece = piece
    self.identity = identity
    self.x = x
    self.y = y
    self.z = z
    self.orientation = orientation
    self.key = key
    self.partner1 = partner1
    self.partner2 = partner2

  def copy(self):
    return(copy.copy(self))

  def loc(self):
    return(self.x, self.y, self.z)

  def reg(self):
      while self.orientation > 3:
        self.orientation -= 3

  def orientate(self, times):
    for i in range(0, times):
      place1 = self.key
      place2 = self.partner1
      place3 = self.partner2
      self.key = place2
      self.partner1 = place3
      self.partner2 = place1
      self.orientation += 1
    self.reg()

  def flip(self):
    placeholder = self.key
    self.key = self.partner1
    self.partner1 = placeholder
    if self.orientation == 1:
      self.orientation == 2
    else:
      self.orientation == 1


#finds piece based on location
def findpiece(x, y, z):
  for i in [wg, wr, wb, wo, gr, rb, bo, og, yg, yr, yb, yo, wgr, wrb, wbo, ygr, yrb, ybo, yog, w, g, r, b, o, yellow]:
    if i.loc() == (x, y, z):
      return(i)  

#finds piece based on identity
def scan(target):
  for i in [wg, wr, wb, wo, gr, rb, bo, og, yg, yr, yb, yo, wgr, wrb, wbo, ygr, yrb, ybo, yog, w, g, r, b, o, yellow]:
    if i.identity == target:
      return(i)

wg = piece(True, 1, 2, 3, 1, 1, 1, 3, 0)
wr = piece(True, 2, 3, 3, 2, 1, 1, 5, 0)
wb = piece(True, 3, 2, 3, 3, 1, 1, 4, 0)
wo = piece(True, 4, 1, 3, 2, 1, 1, 6, 0)
gr = piece(True, 5, 3, 2, 1, 1, 3, 5, 0)
rb = piece(True, 6, 3, 2, 3, 1, 4, 5, 0)
bo = piece(True, 7, 1, 2, 3, 1, 4, 6, 0)
og = piece(True, 8, 1, 2, 1, 1, 3, 6, 0)
yg = piece(True, 9, 2, 1, 1, 1, 2, 3, 0)
yr = piece(True, 10, 3, 1, 2, 1, 2, 5, 0)
yb = piece(True, 11, 2, 1, 3, 1, 2, 4, 0)
yo = piece(True, 12, 1, 1, 2, 1, 2, 6, 0)
wgr = piece(False, 13, 3, 3, 1, 1, 1, 5, 3)
wrb = piece(False, 14, 3, 3, 3, 1, 1, 4, 5)
wbo = piece(False, 15, 1, 3, 3, 1, 1, 6, 4)
wog = piece(False, 16, 1, 3, 1, 1, 1, 3, 6)
ygr = piece(False, 17, 3, 1, 1, 1, 2, 3, 5)
yrb = piece(False, 18, 3, 1, 3, 1, 2, 5, 4)
ybo = piece(False, 19, 1, 1, 3, 1, 2, 4, 6)
yog = piece(False, 20, 1, 1, 1, 1, 2, 6, 3)
w = piece(None, 21, 20, 3, 2, 1, 1, 0, 0)
g = piece(None, 22, 2, 2, 1, 1, 3, 0, 0)
r = piece(None, 23, 3, 2, 2, 1, 5, 0, 0)
b = piece(None, 24, 2, 2, 3, 1, 4, 0, 0)
o = piece(None, 25, 1, 2, 2, 1, 6, 0, 0)
yellow = piece(None, 26, 2, 1, 2, 1, 2, 0, 0)




#R = 1, L = 2, U = 3, D = 4 ,F = 5, B = 6
#normal = 1, prime = 3, twice = 2

def status():
  print("White")
  print(findpiece(1, 3, 3).key, findpiece(2, 3, 3).key, findpiece(3, 3, 3).key)
  print(findpiece(1, 3, 2).key, findpiece(3, 3, 2).key, findpiece(3, 3, 2).key)
  print(findpiece(1, 3, 1).key, findpiece(2, 3, 1).key, findpiece(3, 3, 1).key)
  print("Green")
  print(findpiece(1, 3, 1).partner1, findpiece(2, 3, 1).partner1, findpiece(3, 3, 1).partner2)
  print(findpiece(1, 2, 1).key, findpiece(2, 2, 1).key, findpiece(3, 2, 1).key)
  print(findpiece(1, 1, 1).partner2, findpiece(2, 1, 1).partner1, findpiece(3, 1, 1).partner1)
  print("Red")
  print(findpiece(3, 3, 1).partner1, findpiece(3, 3, 2).partner1, findpiece(3, 3, 3).partner2)
  print(findpiece(3, 2, 1).partner1, findpiece(3, 2, 2).key, findpiece(3, 2, 3).partner1)
  print(findpiece(3, 1, 1).partner2, findpiece(3, 1, 2).partner1, findpiece(3, 1, 3).partner1)
  print("Blue")
  print(findpiece(3, 3, 3).partner1, findpiece(2, 3, 3).partner1, findpiece(1, 3, 3).partner2)
  print(findpiece(3, 2, 3).key, findpiece(2, 2, 3).key, findpiece(1, 2, 3).key)
  print(findpiece(3, 1, 3).partner2, findpiece(2, 1, 3).partner1, findpiece(1, 1, 3).partner1)
  print("Orange")
  print(findpiece(1, 3, 3).partner1, findpiece(1, 3, 2).partner1, findpiece(1, 3, 1).partner2)
  print(findpiece(1, 2, 3).partner1, findpiece(1, 2, 2).key, findpiece(1, 2, 1).partner1)
  print(findpiece(1, 1, 3).partner2, findpiece(1, 1, 2).partner1, findpiece(1, 1, 1).partner1)
  print("Yellow")
  print(findpiece(1, 1, 1).key, findpiece(2, 1, 1).key, findpiece(3, 1, 1).key)
  print(findpiece(1, 1, 2).key, findpiece(1, 1, 2).key, findpiece(3, 1, 2).key)
  print(findpiece(1, 1, 3).key, findpiece(2, 1, 3).key, findpiece(3, 1, 3).key)



#rotates cube
def rotate():
  #moving bottom edges
  edge1 = findpiece(2, 1, 1).identity
  edge2 = findpiece(1, 1, 2).identity
  edge3 = findpiece(2, 1, 3).identity
  edge4 = findpiece(3, 1, 2).identity
  scan(edge1).x -= 1
  scan(edge1).z += 1
  scan(edge2).x += 1
  scan(edge2).z += 1
  scan(edge3).x += 1
  scan(edge3).z -= 1
  scan(edge4).x -= 1
  scan(edge4).z -= 1
  #moving bottom corners
  corner1 = findpiece(3, 1, 1).identity
  corner2 = findpiece(1, 1, 1).identity
  corner3 = findpiece(1, 1, 3).identity
  corner4 = findpiece(3, 1, 3).identity
  scan(corner1).x -= 2
  scan(corner2).z += 2
  scan(corner3).x += 2
  scan(corner4).z -= 2
  #moving top edges
  edge5 = findpiece(2, 3, 1).identity
  edge6 = findpiece(1, 3, 2).identity
  edge7 = findpiece(2, 3, 3).identity
  edge8 = findpiece(3, 3, 2).identity
  scan(edge5).x -= 1
  scan(edge5).z += 1
  scan(edge6).x += 1
  scan(edge6).z += 1
  scan(edge7).x += 1
  scan(edge7).z -= 1
  scan(edge8).x -= 1
  scan(edge8).z -= 1
  #moving top corners
  corner5 = findpiece(3, 3, 1).identity
  corner6 = findpiece(1, 3, 1).identity
  corner7 = findpiece(1, 3, 3).identity
  corner8 = findpiece(3, 3, 3).identity
  scan(corner5).x -= 2
  scan(corner6).z += 2
  scan(corner7).x += 2
  scan(corner8).z -= 2
  #moving centers
  g.x, g.y, g.z = (1, 2, 2)
  o.x, o.y, o.z = (2, 2, 3)
  b.x, b.y, b.z = (3, 2, 2)
  r.x, r.y, r.z = (2, 2, 1)
  #moving edges in e-layer
  edge9 = findpiece(1, 2, 1).identity
  findpiece(1, 2, 1).flip()
  edge10 = findpiece(1, 2, 3).identity
  findpiece(1, 2, 3).flip()
  edge11 = findpiece(3, 2, 3).identity
  findpiece(3, 2, 3).flip()
  edge12 = findpiece(3, 2, 1).identity
  findpiece(3, 2, 1).flip()
  scan(edge9).z += 2
  scan(edge10).x += 2
  scan(edge11).z -= 2
  scan(edge12).x -= 2

def R():
#moving corners
  holder1 = findpiece(3, 1, 1).identity
  scan(holder1).orientate(2)
  scan(holder1).y += 1
  holder2 = findpiece(3, 3, 1).identity
  scan(holder2).orientate(1)
  scan(holder2).z -= 2
  holder3 = findpiece(3, 3, 3).identity
  scan(holder3).orientate(2)
  scan(holder3).y -= 2
  holder4 = findpiece(3, 1, 3).identity
  scan(holder4).orientate(1)
#moving edges
  holder5 = findpiece(3, 2, 1).identity
  scan(holder5).y += 1
  scan(holder5).z += 1
  holder6 = findpiece(3, 3, 2).identity
  scan(holder6).y -= 1
  scan(holder6).z += 1
  holder7 = findpiece(3, 2, 3).identity
  scan(holder7).y -= 1
  scan(holder7).z -= 1
  holder8 = findpiece(3, 1, 2).identity
  scan(holder8).y += 1
  scan(holder8).z -= 1
'''
def L():
#moving corners
  findpiece(1, 1, 1).y += 2
  orientate(findpiece(1, 1, 1), 1)
  findpiece(1, 3, 1).z += 2
  orientate(findpiece(1, 3, 1), 2)
  findpiece(1, 3, 3).y -= 2
  orientate(findpiece(1, 3, 3), 1)
  findpiece(1, 1, 3).y -= 2
  orientate(findpiece(1, 1, 3), 2)
#moving edges
  findpiece(1, 2, 1).z += 1
  findpiece(1, 2, 1).y += 1
  findpiece(1, 3, 2).z += 1
  findpiece(1, 3, 2).y -= 1
  findpiece(1, 2, 3).z -= 1
  findpiece(1, 2, 3).y -= 1
  findpiece(1, 1, 2).z -= 1
  findpiece(1, 1, 2).y += 1



def F():
#moving corners
  findpiece(1, 3, 1).x += 2
  orientate(findpiece(1, 3, 1), 1)
  findpiece(3, 3, 1).y -= 2
  orientate(findpiece(3, 3, 1), 2)
  findpiece(3, 1, 1).x -= 2
  orientate(findpiece(3, 1, 1), 1)
  findpiece(1, 1, 1).y += 2
  orientate(findpiece(1, 1, 1), 2)
#moving edges
  findpiece(2, 3, 1).x += 1
  findpiece(2, 3, 1).y -= 1
  orientate(findpiece(2, 3, 1), 1)
  findpiece(3, 2, 1).x -= 1
  findpiece(3, 2, 1).y -= 1
  orientate(findpiece(3, 2, 1), 1)
  findpiece(2, 1, 1).x -= 1
  findpiece(2, 1, 1).y += 1
  orientate(findpiece(2, 1, 1), 1)
  findpiece(1, 2, 1).x += 1
  findpiece(1, 2, 1).y += 1
  orientate(findpiece(1, 2, 1), 1)

def B():
#moving corners
  findpiece(1, 3, 3).x += 2
  orientate(findpiece(1, 3, 3), 1)
  findpiece(3, 3, 3).y -= 2
  orientate(findpiece(3, 3, 3), 2)
  findpiece(3, 1, 3).x -= 2
  orientate(findpiece(3, 1, 3), 1)
  findpiece(1, 1, 3).y += 2
  orientate(findpiece(1, 1, 3), 2)
#moving edges
  findpiece(2, 3, 3).x -= 1
  findpiece(2, 3, 3).y -= 1
  orientate(findpiece(2, 3, 3), 1)
  findpiece(1, 2, 3).x += 1
  findpiece(1, 2, 3).y -= 1
  orientate(findpiece(1, 2, 3), 1)
  findpiece(2, 1, 3).x += 1
  findpiece(2, 1, 3).y += 1
  orientate(findpiece(2, 1, 3), 1)
  findpiece(3, 2, 3).x -= 1
  findpiece(3, 2, 3).y += 1
  orientate(findpiece(3, 2, 3), 1)'''

'''holder1 = findpiece(3, 1, 1).identity
holder2 = findpiece(3, 3, 1).identity
holder3 = findpiece(3, 3, 3).identity
holder4 = findpiece(3, 1, 3).identity

scan(holder2).orientate(2)
scan(holder2).z -= 2

scan(holder4).orientate(2)
scan(holder4).z += 2

scan(holder1).orientate(1)
scan(holder1).y += 2

scan(holder3).orientate(1)
scan(holder3).y -= 2

status()'''

print(findpiece(2, 1, 2).identity)

print("the code kinda worked i guess")

