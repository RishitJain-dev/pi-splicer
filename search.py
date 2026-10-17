import config
import pifinder
import splicer
## other files working together

import mpmath
## external libraries

final = splicer.splice(config.pidigits, pifinder.pistring)

def search(maxsearch):
    if config.search in final:
        if len(config.search) <= int(maxsearch):
            index_position = final.find(config.search)

            if index_position != -1:
                print(f"we found{config.search}")
                print(f"your phrase is at: {index_position}")

                start = max(0, index_position - 5)
                end = min(len(final), index_position + len(config.search) + 5)
                print(f"translating... {final[start:end]}...")

            else:
                print(f"'{config.search} is not in these digits of pi, please increase the pidigits to find it! (WARNING: THIS WILL TAKE A LONG TIME, POSSIBLY OVER 10 HOURS)")
        else:
            print("too long of a search, will take years to finish")

