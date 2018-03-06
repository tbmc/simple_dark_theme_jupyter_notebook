# To import urllib in a Python 2 and 3 compatible way
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from IPython.core.display import display, HTML

# OneDork
url_style = "https://raw.githubusercontent.com/dunovank/jupyter-themes/master/jupyterthemes/styles/compiled/onedork.css"

# Download CSS
style = urlopen(url_style).read()

# Same for override CSS
url_override = "https://raw.githubusercontent.com/tbmc/simple_dark_theme_jupyter_notebook/master/override_style.css"
style_override = urlopen(url_override).read()

# Apply CSS
display(HTML("""
<style>

    %s
    
    %s

</style>
""" % (style, style_override)))

