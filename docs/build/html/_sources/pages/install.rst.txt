Setup
======

Base Install
-------------

- Download/Install Anaconda: https://www.continuum.io/downloads


Package Dependencies
----------------------

- glob
- sklearn
- pandas
- **wordcloud** (requires install)
- Jupyter Notebook


Installing Dependencies
-------------------------

**Install wordcloud (linux)**

.. code-block:: bash

    conda install -c amueller wordcloud=1.3.1


**Install wordcloud (Windows)**

.. code-block:: bash

    #Download from http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
    pip install wordcloud‑1.3.1‑cp35‑cp35m‑win_amd64.whl


Download Repository
---------------------

.. code-block:: bash

    git clone https://github.com/rayblick/CitationManager


Jupyter Notebook
------------------

.. code-block:: bash

    cd CitationManager
    sudo jupyter notebook

    # Navigate to module-level examples
    # e.g. /dev/bibtex.ipynb


Local Install
---------------
TBA


Command line
--------------
TBA


Additional Notes
-------------------

**Data**

Each module has example data. Default arguments that require data will look in the "data/module/train" or "data/module/test" folders. To get started, you can add two additional folders and specify the new document path when calling each method.

**Example**

- data/module/test/
- data/module/train/
- data/module/yourtestdata/addedfiles
- data/module/yourtraindata/addedfiles


Help
------

1. docs/build/html/pages/reference.html
2. Docstrings
