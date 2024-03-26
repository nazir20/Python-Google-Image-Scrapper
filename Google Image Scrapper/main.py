# Required Libraries
import os
from GoogleImageScraper import GoogleImageScraper

# Paths
webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', 'chromedriver.exe'))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'd2'))

# Search Keys (8)
# [Siberian Husky, Poodle, Labrador Retriever, Golden Retriever, German Shepherd, Dachshund, Bulldog,
# Australian Shepherd]
search_key = "Australian Shepherd"
# Image Properties
number_of_images = 10
headless = False
min_resolution = (0, 0)
max_resolution = (1920, 1080)

image_scraper = GoogleImageScraper(webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
image_urls = image_scraper.find_image_urls()
image_scraper.save_images(image_urls, keep_filenames=True)
