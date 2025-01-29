import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # You can use other browsers as well

# Navigate to Twitter
driver.get("https://twitter.com")

# Wait for the page to load
time.sleep(2)

# Find the search box and enter your hashtag/keyword
search_box = driver.find_element_by_xpath("//input[@aria-label='Search query']")
search_box.send_keys("#your_hashtag_or_keyword")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Scroll down to load more tweets (you may need to repeat this multiple times)
for _ in range(5):  # Adjust the range based on your needs
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load

# Extract tweet data
soup = BeautifulSoup(driver.page_source, "html.parser")
tweets = soup.find_all("div", class_="tweet")

# Process and store data
data = []
for tweet in tweets:
    username = tweet.find("span", class_="username").text.strip()
    timestamp = tweet.find("time")["datetime"]
    text = tweet.find("div", class_="tweet-text").text.strip()
    data.append({"Username": username, "Timestamp": timestamp, "Text": text})

# Create DataFrame
df = pd.DataFrame(data)

# Analyze trends
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Date"] = df["Timestamp"].dt.date
trend_data = df.groupby("Date").size().reset_index(name="Count")

# Visualize data
plt.figure(figsize=(10, 6))
plt.plot(trend_data["Date"], trend_data["Count"])
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.title("Twitter Trend Analysis")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Close the browser
driver.quit()
