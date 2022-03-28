import os
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as fin:
    fout = open('{}'.format(output_file), 'w', encoding='utf-8')
    for line in fin:
        line = line.strip()
        words = line.split(' ')
        words_filtered = []
        for w in words:
            if '[SEP]' in w and len(words_filtered) != 0:
                break
            elif '[SEP]' not in w and '[CLS]' not in w:
                words_filtered.append(w)
        line = ' '.join(words_filtered).replace(' ##', '')
        words = line.split(' ')
        words_filtered = []
        for w in words:
            if '[SEP]' in w and len(words_filtered) != 0:
                break
            elif '[SEP]' not in w and '[CLS]' not in w:
                words_filtered.append(w)
        fout.write('{}\n'.format(' '.join(words_filtered)))
