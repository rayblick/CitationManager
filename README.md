# Evaluate Bibtex Exports

This script converts exported citations to a wordcloud. Note that the wordcloud module can do most of what I have done here so long as the text is extracted in a format that wordcloud expects. This convienence wrapper is made specifically to assess citation exports from JSTOR or similar citation management tool.


### Dependencies

**Install wordcloud (linux)**
```bash
conda install -c amueller wordcloud=1.3.1
```

** Install wordcloud (Windows) **
```python
#Download from : http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
pip install wordcloud‑1.3.1‑cp35‑cp35m‑win_amd64.whl
```


### Data Content 
In this example, the program would skip past this entry because there is no abstract content.

JSTOR CITATION LIST
    
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
     abstract = {},
     language = {English},
     year = {1970},
     publisher = {British Ecological Society},
     copyright = {Copyright © 1970 British Ecological Society},
    }
