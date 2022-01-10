# sentiment_analysis

--- 

### Course Curriculum
#### 00 - Intoduction
1. Intoduction
#### 01 - Reddit Sentiment Trading Bot 1
1.  [x] - Setting up the Evniroment
2.  [x] - Connection to Reddit 
3.  [x] - Get Trending Post & Comments from Reddit
4.  [x] - Stream Comments & Perform Sentiment Analysis
5.  [x] - Trading Stratergy
6.  [x] - Get some Bitcoins $25 NZD got us 0.00038435 BTC
7.  [x] - Connection to Binance in Python
8.  [] - Setting up Order Funtions
9.  [] - Buying Stock Functions
10. [] - Selling Stock Functions

#### 02 - Reddit Sentiment Trading Bot 2
1. [] - Intro to the 2nd trading stratergy
2. [] - Setting up the project
3. [] - Trading Stratergy 2 - Part 1
4. [] - Trading Stratergy 2 - Part 2
5. [] - Trading Straterfy 2 - Part 3
---

### What we've done
0. install conda https://www.youtube.com/watch?v=1mn-vA5l_90
1. Create an python enviroment
    - conda create --name sentimentanalysis python=3.6
    - conda activate sentimentanalysis
    - pip list
2. Connection to Reddit using (PRAW)[https://praw.readthedocs.io/en/stable/]
    - pip install praw
    - https://www.reddit.com/prefs/apps
3. Test things are working
    - `python reddittradingbot1.py`
4. Get some data from the front page
    - [https://praw.readthedocs.io/en/stable/code_overview/reddit/front.html]
    - explore the PRAWS model [https://praw.readthedocs.io/en/stable/code_overview/praw_models.html]
    - stream comments from a subreddit ctr + f =stream [https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html] 
5. Preform sentiment analysis with (TestBlob)[https://textblob.readthedocs.io/en/dev/] NOTE: this is not the best package we are just learning
    -  pip install textblob
    -  polarity between -1-0-1 aka -1  is negative 0 is netural and positive is + 1

--- 