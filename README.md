# Images Downloader

This script allows you to download images from Google Images or scrape URLs of the images based on keywords and other options.

## Prerequisites

- Python 3.x
- pip
- simple_image_downloader

## Installation

1. Clone the repository:

    ```git clone https://github.com/your_username/your_repository.git```

2. Navigate to the project directory:

    ```cd your_repository```

3. Install the required dependencies:

    ```pip install -r requirements.txt```
  
# Usage
```python image_downloader.py -k keyword1 keyword2 -n num_images```

Replace keyword1 and keyword2 with your desired keywords and num_images with the number of images you want to download or scrape URLs for.

## Additional options:

- -e or --engines: Specify the search engines to scrape images from (default: Google).
- -s or --save_dir: Specify the directory to save the downloaded images (default: current working directory).
- -u or --url_scraping: Enable URL scraping instead of image downloading.

# Examples

1. Download 10 images of cats from Google Images:
  ```python image_downloader.py -k cat -n 10```

2. Scrape URLs of 5 images of dogs from Bing and Yahoo:
  ```python image_downloader.py -k dog -n 5 -e bing yahoo -u```

3. Download 20 images of cars and save them in the "images" directory:
  ```python image_downloader.py -k car -n 20 -s images```
  
# License
This project is licensed under the MIT License.










  


  
