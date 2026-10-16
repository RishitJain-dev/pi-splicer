import config
import pifinder
import splicer

pifinder.getpi()
splicer.splice(config.pidigits, pifinder.pistring)