__author__ = 'Jacob Vasu s145473'
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.stem import PorterStemmer
import difflib
import os
from textblob import TextBlob

path = "/Users/s145473/Desktop/summarizer"


def positions(tt):
    list = []
    for i in tt:
        list.append(((len(tt) - tt.index(i)) / len(tt)))
    return list


def labeler(tt, ts):
    list = []
    for i in tt:
        t = 0
        for j in ts:
            if i == j:
                t = 1
                list.append('good')
        if t == 0:
            list.append('bad')
    return list


def sen_len(tt):
    list = []
    maxlen = 0
    for i in tt:
        list.append(len(i.split()))
    for i in list:
        if i > maxlen:
            maxlen = i
    newlist = [x / maxlen for x in list]
    return newlist


def wfis(tt):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tt)
    filtered_sentence = [ps.stem(w) for w in word_tokens if not w in stop_words]

    ws = []
    i = 0
    for w in filtered_sentence:
        if w != '.' or w != '?':
            for w2 in filtered_sentence:
                if w2 == w:
                    i = i + 1
        if w != '.' or w != '?':
            ws.append(i)
            i = 0

    sf = []
    sentences = ' '.join(filtered_sentence)
    sentences = sent_tokenize(sentences)
    i = 0
    for w in sentences:
        for x in sentences:
            y = difflib.SequenceMatcher(None, w, x).ratio()
            if y > 0.8:
                i = i + 1
        sf.append(i)
        i = 0

    while len(ws) != len(sf):
        if len(ws) < len(sf):
            ws.append(1)
        if len(ws) > len(sf):
            ws.pop()

    wfis = [a / b for a, b in zip(ws, sf)]
    return wfis


def sentiment(tok):
    sents = []
    for sentence in tok:
        sent = TextBlob(sentence)
        sents.append(sent.sentiment.polarity)
    return sents


def total(pos, len, wfisf, sent):
    i = 0
    tot = []
    maxtot = 0
    for x in pos:
        if sent[i] >= 0:
            tot.append(pos[i] + (20 * len[i]) + wfisf[i] + (50 * sent[i]))
        if sent[i] < 0:
            tot.append(pos[i] + (20 * len[i]) + wfisf[i] + (-50 * sent[i]))
        i += 1
    for i in tot:
        if i > maxtot:
            maxtot = i
    newtot = [x / maxtot for x in tot]
    return newtot


traindata = []
for file in os.listdir(path):
    if file.startswith("text") and not file.endswith("sum.txt"):
        f1 = open(file, encoding="utf8")
        t1 = f1.read()
        f1.close()
        for filesum in os.listdir(path):
            if filesum.endswith("sum.txt"):
                if (filesum.split("_")[0]) == file.split(".")[0]:
                    f2 = open(filesum, encoding="utf8")
                    t2 = f2.read()
                    f2.close()
                    tt = sent_tokenize(t1)
                    ts = sent_tokenize(t2)
                    label = labeler(tt, ts)
                    pos = positions(tt)
                    senlen = sen_len(tt)
                    wfisf = wfis(t1)
                    sent = sentiment(tt)
                    tot = total(pos, senlen, wfisf, sent)
                    train = []
                    j = 0
                    for i in label:
                        feat = dict(
                            [('position', pos[j]), ('length', senlen[j]), ('wfisf', wfisf[j]), ('sentiment', sent[j]),
                             ('total', tot[j])])
                        train.append((feat, i))
                        j = j + 1
                    traindata.extend(train)

test = []
cl = NaiveBayesClassifier.train(traindata)
f = open("text8.txt", encoding="utf8")
t = f.read()
f.close()
tok = sent_tokenize(t)
pos = positions(tok)
senlen = sen_len(tok)
sent = sentiment(tok)
wfisf = wfis(t)
tot = total(pos, senlen, wfisf, sent)
j = 0
for i in tok:
    feat = dict(
        [('position', pos[j]), ('length', senlen[j]), ('wfisf', wfisf[j]), ('sentiment', sent[j]), ('total', tot[j])])
    if cl.classify(feat) == 'good' or feat['total'] > 0.9:
        print(i)
    j = j + 1
