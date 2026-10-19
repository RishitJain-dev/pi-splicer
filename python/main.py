import python.config as config
import python.pifinder as pifinder
import python.splicer as splicer
import python.search as search

pifinder.getpi()
final = splicer.splice(config.pidigits, pifinder.pistring)
search.search(final, config.maxsearch)