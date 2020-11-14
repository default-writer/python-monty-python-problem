
from random import shuffle, choice

#
N = 5

def Doors(n):
   i = n - 1
   yield 1
   while i > 0:
     yield 0
     i = i - 1

class Monty:
    def __init__(self):
        self.vars = list(Doors(N))
        shuffle(self.vars)

    def open(self):
        return choice([x for x in range(1, N) if x != 0 and not self.vars[x]])

    def check(self, var):
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
      stat2 += m.check(v)
  stat2 = stat2/n
  result2.append(stat2)

print(sum(result1)/10, sum(result2)/10)

# -> 333 666 или около того
