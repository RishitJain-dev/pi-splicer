import config
import mpmath

mpmath.mp.dps = config.pidigits + 2



def getpi(pidigits):
  pi_string = str(mpmath.pi)

  print(pi_string)
  print(f"Found exact pi to {pidigits} digits!")


