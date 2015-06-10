from __future__ import division
from nltk import word_tokenize, Text, FreqDist
from nltk.corpus import stopwords, words
from nltk.corpus import gazetteers
from string import lowercase
import json
from sys import exit, stderr, argv

class TextAccumulator(object):
    def __init__(self):
        self.stopwords = stopwords.words('english')
        self.uscities = set([w.lower() for w in gazetteers.words('uscities.txt')])
        self.usstates = set([w.lower() for w in gazetteers.words('usstates.txt')])
        self.countries = set([w.lower() for w in gazetteers.words('countries.txt')])
        self.basicwords = set(words.words('en-basic'))
        self.paragraph_tokens = []
        self.texts = []

    def process_content(self, content):
        raw = str(' ').join(content['paragraphs'])
        letters = set(lowercase)
        _tokens = []
        for w in word_tokenize(raw):
            lw = w.lower()
            if len(lw) > 2 and lw not in self.uscities and lw not in self.usstates and lw not in self.countries \
                    and lw not in self.stopwords and lw not in self.basicwords and set(lw) <= letters:
                _tokens.append(lw)
        self.texts.append(Text(_tokens))
        self.paragraph_tokens.extend(_tokens)

    def get_stats(self, output_fname):
        fd = FreqDist()
        for text in self.texts:
            fd.update(set(text))

        fh = open(output_fname, 'w')
        text = Text(self.paragraph_tokens)
        fdist = FreqDist(text)
        for (w,f) in fdist.iteritems():
            print >> fh, "%s\t%i" % (w, f)
        fh.close()


def main():
    fh = open(argv[1])
    accu = TextAccumulator()
    while True:
        _length = fh.readline()
        if not _length:
            break

        length = int(_length)
        obj_str = fh.read(length)
        content = json.loads(obj_str)
        fh.read(1)
        accu.process_content(content)
        stderr.write('.')
    print
    accu.get_stats('ht_dict_paragraph.txt')
    return 0

if __name__ == '__main__':
    status = main()
    exit(status)

