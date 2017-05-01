from setuptools import setup

setup(
    name = "CitationManager",
    version = "0.0.1",
    packages = ['bibtex', 'generic'],
    long_description = 'Text processing and classification',
    install_requires = ['pandas','sklearn','wordcloud','glob'],
    include_package_data = True,
    package_data = {'CitationManager': ['data/','static/','output/','docs/']},
    author = "Ray Blick",
    author_email = "rblick.ecol@gmail.com",
    description = 'Text processing and classification',
    keywords = ["Text processing", "NLTK", "natural language", "citations"],
    url = "rayblick.github.io/",
)
