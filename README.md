# Twitch Chat Log Analyzer

[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

## Concerns

Twitch VODs stay for 60 days

## Steps

### Set up Twitch API - DONE

1. Create credentials file for Twitch API
2. Make oauth call
3. Make some sample call

### Get VOD IDs - DONE

1. Get VOD Ids using [Get Videos](https://dev.twitch.tv/docs/api/reference#get-videos)
2. Look at one sample request
3. Extract video ID (May be in `url` field) from past broadcasts
4. Implement loop through pagination
5. Return list of all past broadcasts VOD IDs

### Fetch Chat Logs - DONE

1. Fetch rechat logs using this answer [Get Chat Replay Transcript](https://discuss.dev.twitch.tv/t/getting-chat-replay-transcript/5295/2)
    - Chat replays may not work so try this first honestly.

### Save data in csv form for datasets

1. Create resources/models for comments
2. Save `Comment` model rows as csv for ease of use with pandas dataframes
3. Save Date as well as VOD id
4. Convert json to csv

### Analyzing Data

1. Post dataframe histograms with timestamps
2. Determine how much of chat is noise?
3. Compare viewers with chat

Ideas

- [x] Implement [Burst Detection](https://nikkimarinsek.com/blog/kleinberg-burst-detection-algorithm)
    - Note: Wasn't very useful because it didn't give weights to burst.  It gives a levels for higher bursts so some weight calculation can be made.  Good for creating clips though.
    - Note: Used the FIRST algo in the paper, not the second one created by poster.
- [ ] Create Word Cloud of comments

NLP Ideas

- vectorize comments: https://towardsdatascience.com/understanding-nlp-word-embeddings-text-vectorization-1a23744f7223
- [Create a topic model and see what topics it generates that
correlate to what you're looking for.](https://towardsdatascience.com/covid-19-with-a-flair-2802a9f4c90f)
- [Find examples of chats that fit the topics you are looking for and
use those to train a text classifier to find other chats.](https://towardsdatascience.com/text-classification-with-state-of-the-art-nlp-library-flair-b541d7add21f)


### Notes 2020-7-14

- Ran into issues with comments.  A comment of "No" in comments.json was saved as "NA" in csv, this caused the Sentence(nan) to break when given a nan.
    - Check if passing "No" causes nan issues in dataframe
    - Check if passing "NA" causes nan issues in dataframe

## Experiments

### Experiment 1: Pull Ludwig Chat for Marketing Advice

#### Hypothesis

1. Ludwig has Good Advice on marketing
2. Ludwig doesn't mark when he gives good marketing advice
3. Chat is predictable
4. Chat will spam pepoG when Ludwig is giving marketing advice

So, I can download the chat logs/VODs, search for pepoG and pull out timestamps for good ludwig advice.
Getting Chat Logs from VODs

### Experiment 2: Create Word Cloud to Gain Comment Insight

1. Word Cloud should help show most common words like emotes.

## API Development

- Created Client and API files.  Having second thoughts since it seems like they do the same thing but the client has too much functionality.  Specifically the download vod chat style functions.

Thinking about removing API files and having everything be in the client.

### Notes 2020-11-25

- Added tools for other project (Among Us Game Detector)
- Should move twitch APIs into it's own project
- Should clean up twitchAPI object so you don't have to set headers outside of class construction.
