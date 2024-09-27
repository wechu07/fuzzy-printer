# Fuzzy printer

The aim is simple, to automate printing names on a certificate template, from a list of names provided in a `.csv` file.

## Overview

This project automates the process of generating certificates with names printed on them and converting the resulting images to PDFs. The project uses the following libraries:

- [opencv-python](https://pypi.org/project/opencv-python/): For image processing and manipulation.
- [Pillow](https://pypi.org/project/Pillow/): For rendering text with custom fonts on images.
- [img2pdf](https://pypi.org/project/img2pdf/): For converting images to PDF format.
- [numpy](https://pypi.org/project/numpy/): For numerical operations and image array manipulations.

## Files

### [print.py](print.py)
* Prints the names of the individuals on a JPG file using [opencv-python](https://pypi.org/project/opencv-python/) and [Pillow](https://pypi.org/project/Pillow/).
* Converts the resulting images to PDFs using [img2pdf](https://pypi.org/project/img2pdf/).
* Names are contained in a `.csv` file.

### [clean_csv.py](clean_csv.py)
* Cleans the input `.csv` file by removing numbering and unnecessary whitespace.

### [rename.py](rename.py)
* Renames the awkwardly named files to a preferred name using [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html).

## Usage

1. **Prepare the template**: Generate a certificate template using the software of your choice, then convert it to a JPG file before use. Place the template image in the project directory and name it `template.jpg`.

2. **Clean the CSV file**: Run `clean_csv.py` to clean the input CSV file and generate `cleaned_volunteer_names.csv`.

    ```sh
    python clean_csv.py
    ```

3. **Generate certificates**: Run `print.py` to generate certificates with names printed on them and convert the images to PDFs.

    ```sh
    python print.py
    ```

4. **Rename PDF files**: Run `rename.py` to rename the generated PDF files to a preferred naming convention.

    ```sh
    python rename.py
    ```

## Dependencies

Install the required dependencies using `pip`:

```sh
pip install -r requirements.txt
```


## Example
1. Input CSV: `volunteer names 2024 LNMB.csv`
2. Cleaned CSV: `cleaned_volunteer_names.csv`
3. Generated Certificates: `Stored in generated-certificates-data/`
4. Converted PDFs: `Stored in generated-certificates-data/`
5. Renamed PDFs: `Stored in generated-certificates-data/`

## License
This project is licensed under the MIT License.

