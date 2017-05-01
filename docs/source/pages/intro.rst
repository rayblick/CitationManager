Citation Manager
=================

:Authors:
    Ray Blick
:Version: 0.0.1
:Last update: 2017/05/01

Overview
---------
The "Citation Manager" has two primary objectives. First, to process different types of citation content, such as exported citations from JSTOR (Bitbtex). Second, to provide a text-based prediction algorithm that evaluates titles, abstracts or keywords to predict the labelling of records. For example, evaluate an abstract to identify the most similar journal. This package is compartmentalised into specific standalone modules but share a set of generic helper methods. Setup files are provided for easy install to python. Example data are provided in the /data/ directory and uses namespace convention for module specific content. Share data are stored in /data/shared folder. All of the development for this project was performed using Jupyter Notebook and Atom text editor.

Aim
----
Process citations and predict labelling.

Business Rules
-----------------
- None

Scope
------
- Python Language
- Text processing
- XML processing
- Text classifiers in Sklearn
- Data visualisation (wordclouds)
- Git and Github
- Sphinx documentation
- gh-pages
- Prediction accuracy
- Example lightweight analysis

Out of scope
-------------
- User Interface
- Web application
- Deployment on PyPI

Assumptions
------------
- None

Limitations
-----------
- None

Time Management
----------------
- Any free time

Milestones
------------
- Build project/package layout
- Text-based processing
- Text classifier
- Documentation
- Setup files
