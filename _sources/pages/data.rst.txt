Data
=====

Location
----------

- ./data/

Name spacing
-------------

All folders are separated with module level name spacing.

**Example**

- ./data/bibtex/train/files
- ./data/bibtex/test/files
- ./data/shared/files


Access
-------
Access data using relative links. Default file path and document format are provided.

.. code-block:: python

    # Example code block from bibtex module
    process_citations(docpath='../data/bibtex/train', docformat='txt')
