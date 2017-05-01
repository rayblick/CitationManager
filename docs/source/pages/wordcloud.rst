Wordcloud
==========

Overview
----------
A wordcloud is a visual representation of the words used in a document. This example uses the Bibtex module to process references exported from JSTOR. An image in png format with a transparent background can be used to shape the wordcloud.

Example
--------

.. code-block:: python

    # import wordcloud
    from wordcloud import WordCloud
    from wordcloud import STOPWORDS

    # import custom library
    from CitationManager.bibtex import bibtex as bb
    citations = bb.Bibtex()
    citations.process_citations()

    # Provide a mask
    clip_mask = imread("../static/img/tree.png")

    # Create wordcloud
    wc = WordCloud(background_color="white", width=800,
      height=800, mask=clip_mask, max_words=400, stopwords=STOPWORDS)

    # Generate freq from original words form the first article
    wc.generate_from_frequencies(citations.original_words[0][1])

    # Plot
    plt.figure(figsize=(16,14))
    plt.imshow(wc)
    plt.axis("off")
    plt.show

    # Output to file
    wc.to_file("../output/img/bibtex/tree.png")


Output
-------

.. image:: ../../../output/img/bibtex/tree.png
