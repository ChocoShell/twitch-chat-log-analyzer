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


def main(channel_emotes):
    # Getting Dataframe
    filename = "./data/ludwig/comments/673772949/comments.csv"

    df = pd.read_csv(filename)

    # Generating Wordcloud
    text = " ".join(comment for comment in df.body)

    stopwords = set(STOPWORDS)
    stopwords.update([*FFZ, *TWITCH, *BTTV, *channel_emotes])

    wordcloud = WordCloud(stopwords=stopwords, collocations=False).generate(text)

    # freq_dict = WordCloud(stopwords=stopwords, collocations=False).process_text(text)

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

    wordcloud.to_file("./no_emotes.png")

    # Print wordcloud
    plt.imshow(wordcloud, interpolation="bilinear")

    plt.axis("off")
    plt.show()


def sort_dict(x, descending=False):
    return {
        k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=descending)
    }


ludwig = [
    "ludwig7",
    "ludwigA",
    "ludwigAY",
    "ludwigAwooga",
    "ludwigBANGER",
    "ludwigBRB",
    "ludwigBan",
    "ludwigBlanket",
    "ludwigBoomer",
    "ludwigC",
    "ludwigChan",
    "ludwigChoke",
    "ludwigClam",
    "ludwigCroc",
    "ludwigCute",
    "ludwigD",
    "ludwigDoc",
    "ludwigEZ",
    "ludwigF",
    "ludwigFC",
    "ludwigFarm",
    "ludwigFold",
    "ludwigG",
    "ludwigGamer",
    "ludwigGun",
    "ludwigHands",
    "ludwigHeads",
    "ludwigHi",
    "ludwigHmm",
    "ludwigHypers",
    "ludwigIRS",
    "ludwigJr",
    "ludwigKiss",
    "ludwigLove",
    "ludwigMagnum",
    "ludwigMald",
    "ludwigMelvin",
    "ludwigMilkers",
    "ludwigNarc",
    "ludwigNord",
    "ludwigNyah",
    "ludwigPants",
    "ludwigPeepawhappy",
    "ludwigPeepawsad",
    "ludwigPoggert",
    "ludwigPride",
    "ludwigRelax",
    "ludwigS",
    "ludwigSmooth",
    "ludwigSmug",
    "ludwigStar",
    "ludwigStinky",
    "ludwigT",
    "ludwigTails",
    "ludwigU",
    "ludwigW",
    "ludwigWC",
    "ludwigWow",
    "ludwigYikes",
    "ludwigYuck",
    "ludwigTop",
    "ludwigBottom",
]

main(ludwig)
