import config
## other py file imports

import math
## libraries

k = 1
s = 0


def getpi(pidigits):
  global s, k

  for x in range(pidigits):
    if x % 2 == 0:
      s += 4 / k
    else:
      s -= 4 / k

    k += 2

  print(s)
  print(f"found pi to {pidigits} digits!")


getpi(config.pidigits)