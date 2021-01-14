class queue:
# buinding FIFO class object
  def __init__(self):
    self.items = []
  
  def insert(self, elem):
  # @param elem : T
    self.items.insert(0, elem)
  
  def out(self):
    if not self.empty():
      self.items.pop()
  
  def first(self):
    if not self.empty():
      print self.items[-1]
    else:
      print ""
  
  def last(self):
    if not self.empty():
      print self.items[0]
    else:
      print ""
  
  def empty(self):
  # @return bool
    return len(self.items)==0
  

class stack:
# buinding LIFO class object
  def __init__(self):
    self.items = []
  
  def push(self, elem):
  # @return elem : T
    self.items.insert(0, elem)
  
  def pop(self):
    if not self.empty():
      self.items.reverse()
      self.items.pop()
      self.items.reverse()
  
  def top(self):
    if not self.empty():
      print self.items[0]
    else:
      print ""
  
  def last(self):
    if not self.empty():
      print self.items[-1]
    else:
      print ""
    
  def empty(self):
  # @return bool
    return len(self.items)==0
  
p = stack()
p.push('aa')
p.push('bb')
p.push('cc')
p.top()
p.pop()
p.top()
p.pop()
p.top()
p.pop()
p.top()
print p.empty()
print "..."

p = queue()
p.insert('aa')
p.insert('bb')
p.insert('cc')
p.first()
p.last()
p.out()
p.first()  
p.last()

