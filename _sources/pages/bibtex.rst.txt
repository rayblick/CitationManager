Bibtex Module
===============

Class Name
-----------
- Bibtex


Bound Methods
--------------
The BibTeX module has two methods:

1. process_citations()
2. predict_citation_label()


Method Arguments
-----------------

**process_citations**

- docpath (e.g. '../data/bibtex/train' [default])
- docformat (e.g. txt [default])

**predict_citation_label**

- testpath (e.g. '../data/bibtex/test' [default])
- pattern ('original' or 'stemmed' [default = stemmed])
- targetlabelname (e.g. 'journal' [default])


Usage
-------

.. code-block:: python

    from CitationManager.bibtex import bibtex as bb
    citations = bb.Bibtex()
    # do processing
    citations.process_citations(docpath='../data/bibtex/train', docformat='txt')
    citations.predict_citation_label(pattern="original")


What is BibTeX?
----------------
BibTeX is a file format that describes references. The format of a BibTex document uses "@" syntax such as @article, @book, @inproceedings. A citation export from JSTOR is saved in a txt file format. The special symbols are used in this module to separate the text document prior to text processing and analysis.


BibTeX Format
--------------

.. code-block:: markdown

    @article{1970,
     jstor_articletype = {misc},
     title = {Front Matter},
     author = {},
     journal = {Journal of Ecology},
     jstor_issuetitle = {},
     volume = {58},
     number = {1},
     jstor_formatteddate = {Mar., 1970},
     pages = {pp. i-ii},
     url = {http://www.jstor.org/stable/2258166},
     ISSN = {00220477},
     abstract = {This is a replacement string for this abstract.},
     language = {English},
     year = {1970},
     publisher = {British Ecological Society},
     copyright = {Copyright © 1970 British Ecological Society},
    }

Changes and Updates
---------------------
If you need to make changes to this module then you should focus on two scripts only. These scripts include the module (bibtex.py) and the associated helpers (helpers.py). However, the module mostly calls the functions defined in the helper files so changes will mostly occur there.
