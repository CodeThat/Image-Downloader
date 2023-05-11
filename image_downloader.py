from simple_image_download import simple_image_download as simp
import argparse
import os
import colorama

# Initialize colorama
colorama.init(autoreset=True)

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to print colorized text
def print_colorized(text, color):
    colors = {
        'black': colorama.Fore.BLACK,
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'blue': colorama.Fore.BLUE,
        'magenta': colorama.Fore.MAGENTA,
        'cyan': colorama.Fore.CYAN,
        'white': colorama.Fore.WHITE,
    }
    color_code = colors.get(color, colors['reset'])
    print(f'{color_code}{text}')


# Clear the terminal
clear_terminal()

# Create a response object
response = simp.Downloader

# Define command-line argument parser
parser = argparse.ArgumentParser(
    description='''
Google Images Downloader
# Images are saved in a subdirectory named after each keyword
# Each downloaded image is given a unique name to avoid overwriting existing files
# The saved images can be found in the specified directory or the current working directory
''',
    formatter_class=argparse.RawTextHelpFormatter  # Preserve newlines in description
)

# Add arguments
parser.add_argument('-k', '--keywords', nargs='+', help='Keywords for image search')
parser.add_argument('-n', '--num_images', type=int, help='Number of images to download')
parser.add_argument('-e', '--engines', nargs='+', default=['google'], choices=['google', 'bing', 'yahoo'],
                    help='Search engines to scrape images from (default: Google)')
parser.add_argument('-s', '--save_dir', default='',
                    help='Directory to save the downloaded images (default: current working directory)')
parser.add_argument('-u', '--url_scraping', action='store_true',
                    help='Enable URL scraping instead of image downloading')

# Parse arguments
args = parser.parse_args()

# Check if keywords and number of images are provided
if not args.keywords or not args.num_images:
    parser.print_help()
    exit()

# Determine the save directory
save_directory = args.save_dir if args.save_dir else os.getcwd()

# Clear the terminal again
clear_terminal()

# Colorize the usage output
usage = parser.format_usage()
usage = usage.replace('usage:', f'{colorama.Fore.YELLOW}usage:')

# Print the colorized usage output
print(usage)

# Perform image downloading or URL scraping based on the option chosen
if not args.url_scraping:
    # Pull images for each keyword from all search engines
    for kw in args.keywords:
        for engine in args.engines:
            response().download(kw, args.num_images)
else:
    # Pull URLs of images for each keyword from all search engines, with LIMIT
    for engine in args.engines:
        response().search_urls(' '.join(args.keywords), limit=args.num_images)
        for url in response().cache:
            print_colorized(url, 'green')

