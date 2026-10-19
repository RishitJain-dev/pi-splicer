# config.py

import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)


# define all variables and globals for all other files

pidigits = int(input("10-1000000 (number of digits of pi)"))
## uses 1 million digits of pi
includeasci = False
## (depreciated) chooses whether you can use characters other than space and the alphabet, eg. '^', '#','$'
maxsearch = 20
## (RESTORED) prevents script from taking years to finish by limiting how many characters you can search up at once.
search = ""

banner = pyfiglet.figlet_format("PI    SPLICER", font="bulbhead")
print(f"{Fore.CYAN}{Style.BRIGHT}{banner}")

search = input("enter search term here:")
## enter search here and it will find it

print("Globals configured!")
