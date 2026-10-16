import config
## other files working together

import mpmath
## external libraries


mpmath.mp.dps = config.pidigits + 2
## pi to a certain amount of digits


def getpi(pidigits):
  pi_string = str(mpmath.pi)

  return pi_string
  print(f"Found exact pi to {pidigits} digits!")


