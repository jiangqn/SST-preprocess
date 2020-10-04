import os
import csv

base_path = 'stanfordSentimentTreebank'

if not os.path.exists(base_path):
    os.system('unzip stanfordSentimentTreebank.zip')
    os.system('rm -rf __MACOSX')

dictionary_path = os.path.join(base_path, 'dictionary.txt')

phrase_dictionary_file = open(dictionary_path, 'r', encoding='utf-8')

phrase_dictionary = {}

for line in phrase_dictionary_file.readlines():
    phrase, phrase_id = line.strip().split('|')
    phrase_dictionary[phrase] = int(phrase_id)

sentiment_label_path = os.path.join(base_path, 'sentiment_labels.txt')
sentiment_label_file = open(sentiment_label_path, 'r', encoding='utf-8')

sentiment_dictionary = {}

for i, line in enumerate(sentiment_label_file.readlines()):
    if i == 0:
        continue
    phrase_id, sentiment_value = line.strip().split('|')
    phrase_id = int(phrase_id)
    sentiment_value = float(sentiment_value)
    sentiment_dictionary[phrase_id] = sentiment_value

sentence_path = os.path.join(base_path, 'SOStr.txt')
sentence_file = open(sentence_path, 'r', encoding='utf-8')

data = []

for line in sentence_file.readlines():
    sentence = ' '.join(line.strip().split('|'))
    sentiment = sentiment_dictionary[phrase_dictionary[sentence]]
    data.append((sentence, sentiment))

data_split_path = os.path.join(base_path, 'datasetSplit.txt')
data_split_file = open(data_split_path, 'r', encoding='utf-8')

train_data = []
dev_data = []
test_data = []

for i, line in enumerate(data_split_file.readlines()):
    if i == 0:
        continue
    sentence_id, split_id = line.strip().split(',')
    sentence_id, split_id = int(sentence_id), int(split_id)
    if split_id == 1:
        train_data.append(data[sentence_id - 1])
    elif split_id == 2:
        test_data.append(data[sentence_id - 1])
    else: # split_id == 3:
        dev_data.append(data[sentence_id - 1])

def sst5txt(data, path):
    f = open(path, 'w', encoding='utf-8')
    for sentence, sentiment in data:
        if sentiment <= 0.2:
            label = 0
        elif sentiment <= 0.4:
            label = 1
        elif sentiment <= 0.6:
            label = 2
        elif sentiment <= 0.8:
            label = 3
        else:
            label = 4
        f.write(str(label) + '\t' + sentence + '\n')
    f.close()

def sst5tsv(data, path):
    tsv_data = [['sentence', 'label']]
    for sentence, sentiment in data:
        if sentiment <= 0.2:
            label = 0
        elif sentiment <= 0.4:
            label = 1
        elif sentiment <= 0.6:
            label = 2
        elif sentiment <= 0.8:
            label = 3
        else:
            label = 4
        tsv_data.append([sentence, label])
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(tsv_data)

sst5_base_path = 'SST5'

if not os.path.exists(sst5_base_path):
    os.makedirs(sst5_base_path)

sst5txt(train_data, os.path.join(sst5_base_path, 'train.txt'))
sst5txt(dev_data, os.path.join(sst5_base_path, 'dev.txt'))
sst5txt(test_data, os.path.join(sst5_base_path, 'test.txt'))

sst5tsv(train_data, os.path.join(sst5_base_path, 'train.tsv'))
sst5tsv(dev_data, os.path.join(sst5_base_path, 'dev.tsv'))
sst5tsv(test_data, os.path.join(sst5_base_path, 'test.tsv'))

def sst2txt(data, path):
    f = open(path, 'w', encoding='utf-8')
    for sentence, sentiment in data:
        if sentiment <= 0.4:
            label = 0
        elif sentiment > 0.6:
            label = 1
        else:
            continue
        f.write(str(label) + '\t' + sentence + '\n')
    f.close()

def sst2tsv(data, path):
    tsv_data = [['sentence', 'label']]
    for sentence, sentiment in data:
        if sentiment <= 0.4:
            label = 0
        elif sentiment > 0.6:
            label = 1
        else:
            continue
        tsv_data.append([sentence, label])
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(tsv_data)

sst2_base_path = 'SST2'

if not os.path.exists(sst2_base_path):
    os.makedirs(sst2_base_path)

sst2txt(train_data, os.path.join(sst2_base_path, 'train.txt'))
sst2txt(dev_data, os.path.join(sst2_base_path, 'dev.txt'))
sst2txt(test_data, os.path.join(sst2_base_path, 'test.txt'))

sst2tsv(train_data, os.path.join(sst2_base_path, 'train.tsv'))
sst2tsv(dev_data, os.path.join(sst2_base_path, 'dev.tsv'))
sst2tsv(test_data, os.path.join(sst2_base_path, 'test.tsv'))