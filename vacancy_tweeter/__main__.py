import os
import json

from termcolor import colored
import nltk
import requests

filename = os.path.expanduser('~/.vacancy-tweeter')
url = 'https://data.ox.ac.uk/search/?page_size=10000&q=postdoctoral&type=vacancy'

colormap = {'ORGANIZATION': 'red',
            'PERSON': 'blue',
            'GPE': 'green'}

try:
    with open(filename, 'r') as f:
        vacancies = json.load(f)
except IOError:
    vacancies = requests.get(url, headers={'Accept': 'application/json'}).json()
    with open(filename, 'w') as f:
        json.dump(vacancies, f, indent=2)

vacancies = [h['_source'] for h in vacancies['hits']['hits']]

for vacancy in vacancies:
    desc = vacancy['description']
    tokens = nltk.word_tokenize(desc)
    tagged = nltk.pos_tag(tokens)
    try:
        chunks = nltk.chunk.ne_chunk(tagged)
        for chunk in chunks:
            if isinstance(chunk, nltk.tree.Tree):
                print colored(' '.join(c[0] for c in chunk), colormap[chunk.node]),
            elif chunk[0].lower() == 'group':
                print colored(chunk[0], 'yellow'),
            elif chunk[0].lower() in ('study', 'investigate'):
                print colored(chunk[0], 'orange'),
            elif chunk[0].lower() == 'research':
                print colored(chunk[0], 'cyan'),
            else:
                print chunk[0],
        print
        print '-'*80
    except:
        pass
