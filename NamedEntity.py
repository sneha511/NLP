from collections import defaultdict
import itertools as it

from nltk import ne_chunk
import codecs
with codecs.open('post_all.csv',encoding='latin-1') as f:
    sample_review=list(it.islice(f, 7, 9))[0]
 #   sample_review=f.read()
    sample_review=sample_review.replace('\\n', '\n')
    #print sample_review


def nltk_entities(fileids=None, section = None,corpus=sample_review):
    """
    Extract entities using the NLTK named entity chunker.
    """
    results = defaultdict(lambda: defaultdict(list))
    fileids = id or corpus.id()

    for fileid in fileids:
        if section is not None:
            text = nltk.pos_tag(nltk.word_tokenize(list(sectpull([fileid],section=section))[0][1]))
        else:
            text = nltk.pos_tag(corpus.words(fileid))



        for entity in nltk.ne_chunk(text):
            if isinstance(entity, nltk.tree.Tree):
                etext = " ".join([word for word, tag in entity.leaves()])
                label = entity.label()
            else:
                continue

            if label == 'PERSON':
                key = 'persons'
            elif label == 'ORGANIZATION':
                key = 'organizations'
            elif label == 'LOCATION':
                key = 'locations'
            elif label == 'GPE':
                key = 'other'
            else:
                key = None

            if key:
                results[fileid][key].append(etext)

    return results
nltkents = nltk_entities(corpus.id, section='top')
