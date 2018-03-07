# To import urllib in a Python 2 and 3 compatible way
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from IPython.core.display import display, HTML

# Same for override CSS
url_override = "https://raw.githubusercontent.com/tbmc/simple_dark_theme_jupyter_notebook/master/override_style.css"
style_override = urlopen(url_override).read()

# Apply CSS
display(HTML("""
<style>
    %s
</style>
""" % style_override))
