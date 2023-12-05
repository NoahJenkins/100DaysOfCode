from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("detach", True)

# Create a Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # URL of the Dino game
    url = 'https://elgoog.im/dinosaur-game/'
    driver.get(url)

    # Wait for the game to load (adjust the sleep time if needed)
    time.sleep(2)

    # Send spacebar key to start the game
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.SPACE)

    while True:
        # Get screenshot of the game area
        screenshot = driver.get_screenshot_as_png()
        with open("screenshot.png", "wb") as file:
            file.write(screenshot)

        # Load the screenshot
        screenshot = Image.open("screenshot.png")

        # Define the region where the obstacles are located based on the game's position
        # You may need to adjust these coordinates based on your screen resolution
        obstacle_area = (215, 360, 265, 390)  # Adjust these values accordingly

        # Crop the screenshot to focus on the obstacle area
        obstacle = screenshot.crop(obstacle_area)

        # Analyze the obstacle image to check for obstacles (cacti, birds, etc.)
        # Here, you'd use image recognition or pixel analysis to detect obstacles
        # You might use libraries like OpenCV or implement your own logic to recognize obstacles
        # This example assumes a simple pixel color analysis, which may not be accurate in all cases
        obstacle_pixels = obstacle.load()
        has_obstacle = any(obstacle_pixels[x, y] != (255, 255, 255) for x in range(obstacle.width) for y in range(obstacle.height))

        if has_obstacle:
            # If an obstacle is detected, simulate jumping by pressing the spacebar
            body.send_keys(Keys.SPACE)

        time.sleep(0.1)  # Adjust the delay between checks

except Exception as e:
    print(e)
    # You may handle exceptions here if needed
