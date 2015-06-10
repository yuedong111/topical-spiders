from __future__ import division
from nltk import word_tokenize, Text
import sys

class TopicClassifier(object):
    def __init__(self, prob_dict):
        fh = open(prob_dict)
        _sum = 0
        self.topic = {}
        for line in fh:
            (word, sep, freq) = line.strip().partition('\t')
            freq_int = int(freq)
            self.topic[word] = freq_int
            _sum += freq_int

        for (k, v) in self.topic.iteritems(): self.topic[k] = v / float(_sum)

    def classify_paragraphs(self, paragraphs):
        topic_probability = 0.0
        for p in paragraphs:
            for token in word_tokenize(p):
                if token in self.topic:
                    topic_probability += self.topic[token]
        if topic_probability > 0.1:
            return True
        return False


if __name__ == '__main__':
    tc = TopicClassifier(sys.argv[1])
    print tc.topic['escorts']