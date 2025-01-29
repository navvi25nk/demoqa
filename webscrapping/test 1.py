from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path="./chromedriver")

# Function to search for hashtag/keyword
def search_twitter(hashtag):
    url = f"https://twitter.com/search?q=%23{hashtag}&src=typed_query"
    driver.get(url)
    time.sleep(3)  # Adjust as needed

# Function to scroll and load more tweets
def scroll_and_load():
    body = driver.find_element_by_tag_name('body')
    for _ in range(5):  # Adjust as needed
        body.send_keys(Keys.END)
        time.sleep(2)  # Adjust as needed

# Function to scrape tweets
def scrape_tweets(num_tweets):
    scroll_and_load()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tweets = soup.find_all('div', {'data-testid': 'tweet'})

    data = []
    for tweet in tweets[:num_tweets]:
        tweet_text = tweet.find('div', {'lang': 'en'}).text.strip()
        user = tweet.find('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'}).text.strip()
        timestamp = tweet.find('time')['datetime']
        data.append({'User': user, 'Timestamp': timestamp, 'Tweet': tweet_text})

    return pd.DataFrame(data)

# Function to visualize data trends
def visualize_data(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.date
    tweet_counts = df['Date'].value_counts().sort_index()
    plt.plot(tweet_counts.index, tweet_counts.values)
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.title('Trend of Tweets Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function
def main():
    hashtag = input("Enter the hashtag or keyword you want to search for: ")
    search_twitter(hashtag)
    num_tweets = int(input("Enter the number of tweets to scrape: "))
    df = scrape_tweets(num_tweets)
    print(df.head())
    visualize_data(df)

# Execute main function
if __name__ == "__main__":
    main()

# Close WebDriver
driver.quit()
