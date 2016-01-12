from nltk.classify import NaiveBayesClassifier
import nltk
from datetime import timedelta
from document.models import Document
from stock_retrieval.models import ShareValue

minutes_after = [0, 5, 20, 40, 60, 100, 160, 260, 420, 680]


# from nltk.sentiment import SentimentAnalyzer http://www.nltk.org/howto/sentiment.html


def word_feats(words):
    return dict([(word, True) for word in words])


def get_impact(document):
    # get share value before article
    value_before = ShareValue.objects.filter(share=document.share, time__lt=document.published).order_by(
        'time').last().price

    # get share value x time after article
    price_after = ShareValue.objects.filter(share=document.share,
                                            time__gt=document.published + timedelta(minutes=20)).order_by(
        'time').first().price

    if price_after > value_before:
        impact = 'pos'
    elif value_before > price_after:
        impact = 'neg'
    else:
        impact = 'neu'

    document.sentiment = impact
    document.save()
    return


def get_nltktext(text):
    tokens = nltk.word_tokenize(text)
    return nltk.Text(tokens)


def train():
    # only articles for which the impact can be calculated are relevant
    known_data = Document.objects.filter(published__gt=ShareValue.objects.order_by('time').first().time,
                                         published__lt=ShareValue.objects.order_by('time').last().time + timedelta(
                                             minutes=20))

    # get impact for documents for which it has not been computed yet
    for document in known_data.filter(sentiment__isnull=True):
        get_impact(document)

    known_data_count = known_data.count()

    # 2/3 training data
    num_training_data = int(round(2 * known_data_count / 3))
    training_feats = []
    for document in known_data[:num_training_data]:
        text = get_nltktext(document.text)
        training_feats.append((word_feats(text), document.sentiment))

    classifier = NaiveBayesClassifier.train(training_feats)

    # 1/3 test_data
    num_testing_data = int(round(known_data_count / 3))
    testing_feats = []
    for document in known_data[num_training_data:num_testing_data]:
        text = get_nltktext(document.text)
        training_feats.append((word_feats(text), document.sentiment))

    print('train on %d instances, test on %d instances' % (len(training_feats), len(testing_feats)))

    print('accuracy:', nltk.classify.util.accuracy(classifier, testing_feats))
    classifier.show_most_informative_features()

    return classifier


def classify(classifier):
    for document in Document.objects.new_data():
        text = get_nltktext(document.text)
        result = classifier.classify(word_feats(text))
        document.document.predicted_sentiment = result
        document.save()
