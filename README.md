# Fuzzy printer

The aim is simple, to automate printing names on a certificate template, from a list of names provided on an .txt file.

I used a free JPG to PDF converter, that individually converted the resulting files into separate PDFs that need renaming. I recognize that this is probably old school anyway, and the resulting filenames was a disaster.

[print.py](print.py)
* Prints the names of the individuals on a JPG file using [opencv-python](https://pypi.org/project/opencv-python/)
    * Names are contained in an MS Excel file or Google sheets file

[rename.py](rename.py)
* Renames the awkwardly names files to a preferred name using [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

Generate a template using the software of your choice, then convert it to a JPG file before use.