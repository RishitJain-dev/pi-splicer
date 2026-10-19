import python.config as config
## other files working together

import mpmath
## external libraries


mpmath.mp.dps = config.pidigits + 2
  ## pi to a certain amount of digits
pistring = str(mpmath.pi)


def getpi():
  return pistring



