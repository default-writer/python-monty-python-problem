
from random import shuffle, choice
#
# Monty's chances improvements are
#
# imrovement is 1/n*(n-2) so chances are 1/n + 1/n(n-2) = (n-1)/n(n-2)
#
N = 3
# at 10 doors it is 1/n*(n-2) or 0.0125 chances improvement
# at 9 it is 0.(015873) chances improvement
# at 8 it is 0.0208(3) chances improvement
# at 7 it is 0.0(285714) chances improvement
# at 6 it is 0.041(6) chances improvement
# at 5 it is 0.0(6) chances improvement
# at 4 it is 0.125 chances improvement
# at 3 it is 0.(3) chances improvement

# door generator
def Doors(n):
  i = n - 1
  yield 1
  while i > 0:
    yield 0
    i = i - 1

class Monty:
  def __init__(self):
    """Create 1 in random position"""
    self.vars = list(Doors(N))
    shuffle(self.vars)

  def open(self):
    """Select any other door, than chosen by default"""
    return choice([x for x in range(1, N) if not self.vars[x]])

  def check(self, var=0):
    return self.vars[var]

n = 1000

result1 = []
for i in range(10):
  stat1 = 0
  for _ in range(n):
      m = Monty()
      stat1 += m.check(0)
  stat1 = stat1/n
  result1.append(stat1)

result2 = []
for i in range(10):
  stat2 = 0
  for _ in range(n):
      m = Monty()
      h = m.open()
      v = choice([x for x in range(1, N) if x != h])
      #stat2 += m.check() # this will return the same success rates
      stat2 += m.check(v) # this will return imporved success rates
  stat2 = stat2/n
  result2.append(stat2)


# -> 0.2 0.267 respectively
print(sum(result1)/10, sum(result2)/10)
