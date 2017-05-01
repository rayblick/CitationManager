Project Layout
===============

Modules
--------
- bibtex
- generic

Module Helpers
---------------
All processing specific to a module is stored in a helper file and the code is reduced to a minimum in the module itself.

Name spacing
-------------
All folders are separated with module level name spacing.

**Examples**

- ./data/bibtex/files
- ./data/othermodule/files
- ./output/bibtex/files
- ./output/othermodule/files

Generic Helpers
----------------
Generic helpers are not module specific and are implemmented in more than one module. It should be noted here that changes to these functions may affect the performance/functionality of more than one module. Generic helpers live in a neighbouing folder and the relative path names are imported using sys.path.append('..').

Structure
-----------

.. code-block:: bash

  CitationManager
    │
    ├───bibtex
    │   ├───__init__.py
    │   ├───bibtex.py
    │   └───helpers.py
    │
    ├───data
    │   ├───bibtex
    │   │    ├───test
    │   │    ├───train
    │   │    └───README.txt
    │   │
    │   └───shared
    │
    ├───dev
    │   ├───.ipynb_checkpoints
    │   ├───Exploration.ipynb
    │   └───Testing.ipynb
    │
    ├───docs
    │   ├───build
    │   │   └───html #Docs start at index.html
    │   └───source
    │       └───pages
    │
    ├───generic
    │   ├───__init__.py
    │   └───helpers.py
    │
    ├───static
    │   └───img
    │
    ├───output
    │   └──bibtex
    │
    ├───__init__.py
    ├───README.md #Github landing page
    └───...#Project build files


Documentation
---------------

- Github landing page (./README.md)
- Sphinx documentation (./docs)
- Document strings
- Comment lines


Updating documentation
------------------------

**Windows**

.. code-block:: bash

    git checkout gh-pages
    del .git\index
    git clean -fdx
    echo. 2>.nojekyll
    git checkout master docs/build/html
    xcopy .\docs\build\html\* .\ /E
    rmdir /S docs
    git add -A
    git commit -m "publishing docs"
    git push origin gh-pages


**Linux**

.. code-block:: bash

    git checkout gh-pages
    rm -rf .
    touch .nojekyll
    git checkout master docs/build/html
    mv ./docs/build/html/* ./
    rm -rf ./docs
    git add --all
    git commit -m "publishing docs"
    git push origin gh-pages



Docstrings
-----------
Each method has a break down of its applicaiton.

**Example (generic helper method)**

.. code-block:: python

    def remove_stopwords(dictionary):
        """
        Removes single letters (e.g. 'a') and stop words (e.g. 'the').

        Parameters
        ----------
        arg1: dictionary of word-count pairs.

        Exceptions
        ----------
        Try to stem each word. Exception returns the original word.

        Usage
        -----
        remove_stopwords({'running': 5})

        Returns
        -------
        Two dictionaries;
            1) original words
            2) stemmed words
        ({'running': 5}, {'run': 5})

        Doctest
        -------
        >>> remove_stopwords({'this':1, 'running':5, 'testing': 2})
        ({'running': 5, 'testing': 2}, {'run': 5, 'test': 2})

        """
        # Processing...
