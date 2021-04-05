import torch

from flair.embeddings import (
    FlairEmbeddings,
    DocumentPoolEmbeddings,
    BertEmbeddings,
)
from flair.data import Sentence
from tqdm import tqdm


def validate_text(series):
    print("Validating text...")
    length = len(series)
    for i in range(length):
        try:
            Sentence(series[i])
        except Exception:
            print(i)


def generate_topics_on_series(series):
    """https://towardsdatascience.com/covid-19-with-a-flair-2802a9f4c90f

    Returns:
        [type]: [description]
    """
    validate_text(series)

    # initialise embedding classes
    flair_embedding_forward = FlairEmbeddings("news-forward")
    flair_embedding_backward = FlairEmbeddings("news-backward")
    bert_embedding = BertEmbeddings("bert-base-uncased")

    # combine word embedding models
    document_embeddings = DocumentPoolEmbeddings(
        [bert_embedding, flair_embedding_backward, flair_embedding_forward]
    )

    # set up empty tensor
    X = torch.empty(size=(len(series.index), 7168)).cuda()

    # fill tensor with embeddings
    i = 0
    for text in tqdm(series):
        sentence = Sentence(text)
        document_embeddings.embed(sentence)
        embedding = sentence.get_embedding()
        X[i] = embedding
        i += 1

    X = X.cpu().detach().numpy()
    torch.cuda.empty_cache()

    return X
