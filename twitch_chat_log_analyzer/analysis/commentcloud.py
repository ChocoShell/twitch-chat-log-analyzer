# External imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Local Imports
from twitch_chat_log_analyzer.json_utils import write_json_file
from .emotes import FFZ, TWITCH, BTTV


def sort_dict_by_values(x, descending=False):
    return {
        k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=descending)
    }


def get_most_common_words(comments, collocations=False, n=100):
    text = " ".join(comment for comment in comments)

    most_common_words = WordCloud(stopwords=STOPWORDS, collocations=collocations).process_text(text)

    return sort_dict_by_values(most_common_words, descending=True)

    # ffz_words = {}
    # twitch_words = {}
    # bttv_words = {}

    # for k, v in freq_dict.items():
    #     if k in FFZ:
    #         ffz_words[k] = v
    #     elif k in TWITCH:
    #         twitch_words[k] = v
    #     elif k in BTTV:
    #         bttv_words[k] = v

    # all_emotes = {**ffz_words, **twitch_words, **bttv_words}

    # write_json_file(sort_dict(ffz_words, True), "ffz_words.json", sort_keys=False)
    # write_json_file(sort_dict(twitch_words, True), "twitch_words.json", sort_keys=False)
    # write_json_file(sort_dict(bttv_words, True), "bttv_words.json", sort_keys=False)
    # write_json_file(sort_dict(all_emotes, True), "all_emotes.json", sort_keys=False)

    # Visualizing Word Cloud
    # write_json_file(freq_dict, "freq_673772949.json", sort_keys=False)

    # wordcloud.to_file("./no_emotes.png")

    # # Print wordcloud
    # plt.imshow(wordcloud, interpolation="bilinear")

    # plt.axis("off")
    # plt.show()

# bots = ["Nightbot", "StreamElements"]

# no_nightbot_df = filter_out_commentors(bots)

# cleaned_df = no_nightbot_df

# lowered_df = filter_sub_messages(df)

# # lowered_df["body"] = lowered_df.body.str.lower()
# cleaned_subs_df = lowered_df
# cleaned_of_subs_df = cleaned_subs_df[~cleaned_subs_df.body.str.startswith("!")]


# # Getting Dataframe
# filename = "./comments.csv"
# channel = "ludwig"

# df = pd.read_csv(filename)
