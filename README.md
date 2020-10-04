# SST-preprocess

This is a python script for converting Stanford Sentiment Treebank dataset (https://nlp.stanford.edu/sentiment/index.html) to common used text classification format.

The ```stanfordSentimentTreebank.zip``` file is download from (http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip).

In the fine-grained sentiment classification dataset SST5, ```0, 1, 2, 3, 4``` represent ```very negative, negative, neutral, positive, very positive``` respectively.

In the binary sentiment classification dataset SST2, ```0, 1``` represent ```negative, positive``` respectively.

The statistics of dataset split for SST5 and SST2 are shown below.

| Dataset | SST5 | SST2 |
| ---- | ---- | ----  |
| Train | 8544 | 6920 |
| Dev | 1101 | 872 |
| Test | 2210 | 1821 |