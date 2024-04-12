from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image, ImageDraw

def capture_screenshot(url, output_file):
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Take a screenshot
    driver.save_screenshot(output_file)

    # Close the browser
    driver.quit()

def extract_html(url):
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Extract the HTML content
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    return html_content

def compare_html(actual_html, expected_html, screenshot_file):
    actual_soup = BeautifulSoup(actual_html, 'html.parser')
    expected_soup = BeautifulSoup(expected_html, 'html.parser')

    # Compare the parsed soup objects
    if actual_soup == expected_soup:
        print("HTML content matches!")
    else:
        print("HTML content differs.")

    # Highlight visible areas in the screenshot
    img = Image.open(screenshot_file)
    draw = ImageDraw.Draw(img)

    # Example: Draw a red rectangle around the header
    header_coords = (100, 50, 600, 150)  # Adjust coordinates as needed
    draw.rectangle(header_coords, outline="red", width=2)

    # Save the modified screenshot
    img.save("highlighted_screenshot.png")
    print("Saved highlighted screenshot as 'highlighted_screenshot.png'")

if __name__ == "__main__":
    # Example usage
    target_url = "http://example.com"
    screenshot_file = "website_screenshot.png"
    expected_html = "<html><head>...</head><body>...</body></html>"

    capture_screenshot(target_url, screenshot_file)
    actual_html = extract_html(target_url)
    compare_html(actual_html, expected_html, screenshot_file)



# Another attempt

from bs4 import BeautifulSoup
from selenium import webdriver

def capture_screenshot(url, output_file):
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Take a screenshot
    driver.save_screenshot(output_file)

    # Close the browser
    driver.quit()

def extract_html(url):
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Extract the HTML content
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    return html_content

def compare_html(actual_html, expected_html):
    actual_soup = BeautifulSoup(actual_html, 'html.parser')
    expected_soup = BeautifulSoup(expected_html, 'html.parser')

    # Compare the parsed soup objects
    if actual_soup == expected_soup:
        print("HTML content matches!")
    else:
        print("HTML content differs.")

if __name__ == "__main__":
    # Example usage
    target_url = "http://example.com"
    screenshot_file = "website_screenshot.png"
    expected_html = "<html><head>...</head><body>...</body></html>"

    capture_screenshot(target_url, screenshot_file)
    actual_html = extract_html(target_url)
    compare_html(actual_html, expected_html)



# Othet option



import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        self.load(QUrl(url))
        self.wait_load()  # Wait for the page to load
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        image.save(output_file)
        print(f'Saved screenshot as {output_file}')

    def wait_load(self, delay=0):
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True

# Example usage:
s = Screenshot()
s.capture('http://example.com', 'website_screenshot.png')

from selenium import webdriver

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://example.com')

# Take a screenshot
driver.save_screenshot('website_screenshot.png')

# Close the browser
driver.quit()

