# Library Genesis Book URL Fetcher

This is a simple Python GUI application built using Tkinter for fetching book URLs from Library Genesis using the libgen-api.

## Introduction

Library Genesis is a website that provides free access to millions of research articles and books. This application allows users to search for books and retrieve their direct download URLs from Library Genesis using the libgen-api.

## Features

- Simple GUI interface for easy interaction.
- Search for books by author.
- Fetch direct download URLs for books from Library Genesis.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- libgen-api (`pip install libgen-api`)

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Samreen-Kazi/libgen-gui.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the directory where you cloned the repository:

    ```
    cd library-genesis-book-url-fetcher
    ```

2. Run the application:

    ```
    python main.py
    ```

3. Enter the book title.
4. Click on the "Search" button.
5. The direct download URL(s) for the book(s) will be displayed in the output area.

## Acknowledgments

- [Library Genesis](http://libgen.rs/)
- [libgen-api](https://pypi.org/project/libgen-api/)
