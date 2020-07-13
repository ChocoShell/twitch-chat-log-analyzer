# Twitch Chat Log Analyzer

## Pull Ludwig Chat Advice

1. Ludwig has Good Advice on marketing 
2. Ludwig doesn't mark when he gives good marketing advice 
3. Chat is predictable 
4. Chat will spam pepoG when Ludwig is giving marketing advice 

So, I can download the chat logs/VODs, search for pepoG and pull out timestamps for good ludwig advice.
Getting Chat Logs from VODs

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

### Save data in csv form for datasets instead of json.

1. Create resources/models for comments
2. Save `Comment` model rows as csv for ease of use with pandas dataframes
3. Save Date as well as VOD id

### Analyzing Data

1. Post dataframe histograms with timestamps
2. Determine how much of chat is noise?
3. Compare viewers with chat

Need to brainstorm more ideas on analyzing chat
