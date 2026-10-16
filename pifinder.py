import config
## other files working together

import mpmath
## external libraries


mpmath.mp.dps = config.pidigits + 2
## pi to a certain amount of digits


def getpi(pidigits):
  pistring = str(mpmath.pi)

  return pistring
  print(f"Found exact pi to {pidigits} digits!")


