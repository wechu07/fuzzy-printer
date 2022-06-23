# Fuzzy printer

This project is based on the Python programming language. AIm is simple, to automate printing names on a certificate template, from a list of names provided on an Excel/ Google Sheets file.\

I used a free JPG to PDF converter, that individually converted the resulting files into separate PDFs that need renaming. I recognize that this is probably old school anyway.

[print](print.py)
* Prints the names of the individuals on a JPG file using [opencv-python](https://pypi.org/project/opencv-python/)
    * Names are contained in an MS Excel file or Google sheets file

[rename](rename.py)
* Renames the awkwardly names files to a preferred name using [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)