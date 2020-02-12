import os
import sys
from pathlib import Path

HOME_DIR = Path.home()

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.plantuml",
]
source_suffix = ".rst"
master_doc = "index"
project = "Python Design Patterns"
year = "2020"
author = "Johan Vergeer"
copyright = f"{year}, {author}"
version = release = "0.1.0"
nitpicky = True

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/johanvergeer/python-design-patterns/issues/%s", "#"),
    "pr": ("https://github.com/johanvergeer/python-design-patterns/pull/%s", "PR #"),
}

rst_epilog = """
.. role:: raw-html(raw)
   :format: html

.. |gof_dp| replace:: :raw-html:`<a href="http://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612" target="_blank">Design Patterns: Elements of Reusable Object-Oriented Software</a>`
.. |j2ee_dp| replace:: :raw-html:`<a href="http://www.amazon.com/J2EE-Design-Patterns-William-Crawford/dp/0596004273/ref=sr_1_2" target="_blank">J2EE Design Patterns</a>`
.. |jdp| replace:: :raw-html:`<a href="https://github.com/iluwatar/java-design-patterns" target="_blank">Java Design Patterns</a>`
"""

xref_links = {"key": ("link text", "URL")}

xref_links.update(
    {
        "gof_dp": (
            "Design Patterns: Elements of Reusable Object-Oriented Software",
            "http://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612",
        )
    }
)

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = "sphinx_rtd_theme"

else:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    src_dir = os.path.join(os.path.dirname(dir_path), "src")
    # Append src dir when building on RTD
    sys.path.insert(0, src_dir)

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html", "sourcelink.html"],
}
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

# PLANT UML
plantuml = f'java -jar {HOME_DIR.absolute() / "workspace" / "plantuml.jar"}'

# SPHINX TODO PLUGIN

todo_emit_warnings = True
