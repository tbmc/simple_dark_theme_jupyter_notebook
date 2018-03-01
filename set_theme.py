# To import urllib in a Python 2 and 3 compatible way
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from IPython.core.display import display, HTML

# OneDork
# For original style: url_style = "https://raw.githubusercontent.com/dunovank/jupyter-themes/master/jupyterthemes/styles/compiled/onedork.css"
url_style = "https://goo.gl/wYuXtc"
# Download CSS
style = urlopen(url_style).read()

# Apply CSS
display(HTML("<style>%s</style>" % style))

# Remove borders ! It's better for side by side documents
display(HTML("""
<style>
    /* Modifications to notebook format  */
    #notebook { padding-top: 0px !important; } /* eliminate top gray */
    .container { width:100% !important;     } /* eliminate side gray */
    .end_space { min-height: 800px !important; } /* eliminate bottom gray */
    .input .input_prompt.prompt { min-width: 0; } /* reduce size of the In [n] */
    div.output_area pre { font-size: 16px !important; padding-left: 10px; }
</style>
"""))
