A = ["grande", "medio", "piccolo", "minuscolo"]
B = []
C = []
hanoiTowers = [A,B,C]

def forwardSwap(towers):
# @param towers : List
# @return list
  if len(towers[2])==0 and len(towers[0])==1:
    return towers

  #check
  elif len(towers[1]) == 1 and len(towers[2]) == 1 and len(towers[0]) > 1:
    elem = towers[2].pop()
    towers[1].append(elem)
    print ("Movo da C a B \n", towers)
    return forwardSwap(towers)

  elif len(towers[0]) == 1:
    elem = towers[2].pop()
    towers[1].append(elem)
    print ("Movo da C a B \n", towers)
    return forwardSwap(towers)

  else:
    elem = towers[0].pop()
    if len(towers[2]) == 0:
      towers[2].append(elem)
      print ("Movo da A a C \n", towers)
    else:
      towers[1].append(elem)
      print ("Movo da A a B \n", towers)
    return forwardSwap(towers)


def middleSwap(towers):
# @param towers : List
# @return list
  elem = towers[0].pop()
  towers[2].append(elem)
  print ("Muovo da B ad A \n", towers)
  return towers


def backwardSwap(towers):
# @param towers : List
# @return list
  if len(towers[2]) == 3:
    return towers
  elif len(towers[1]) != 0:
    elem = towers[1].pop()
    if len(towers[0]) == 0:
      towers[0].append(elem)
      print ("Muovo da B ad A\n", towers)
    else:
      towers[2].append(elem)
      print ("Muovo da B a C\n", towers)
    return backwardSwap(towers)
  else:
    elem = towers[0].pop()
    towers[2].append(elem)
    print ("Muovo da A ad C\n", towers)
    return backwardSwap(towers)


def muoviTorri(towers):
# @param towers : List
# @return list
  assert len(towers) == 3

  if len(towers[2])==3:
    print ("FINE")
    return

  elif len(towers[0]) > 1:
    towers = forwardSwap(towers)

  elif len(towers[2]) == 1:
    towers = backwardSwap(towers)

  else: # len(towers[1]) > 1
    towers = middleSwap(towers)
  muoviTorri(towers)

print (hanoiTowers)
muoviTorri(hanoiTowers)
