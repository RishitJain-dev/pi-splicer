import config
import pifinder
import splicer
import search

pifinder.getpi()
splicer.splice(config.pidigits, pifinder.pistring)
search.search(config.maxsearch)