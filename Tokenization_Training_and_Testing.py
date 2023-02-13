# This Python file uses the following encoding: utf-8

import re
import codecs
import string
import unicodedata
import pycrfsuite
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


sentences = list()
f = codecs.open('CombinedDataset.txt', 'r', encoding='utf-8')
for line in f:
    sentences.append(line)
f.close()

print ("No. of sentences in the dataset:",len(sentences))
print(sentences)



def sentence_making(sentence):

    word_lenghts = []
    positions = []
    all_chars = []
    all_positions = []

    sentence_split = sentence.split(" ")
    for l in sentence_split:
        word_lenghts.append(len(l))


    chr_start = 0
    for length in word_lenghts:
        chr_start = chr_start + length
        positions.append(chr_start)
    concatenated = sentence.replace(" ", "")


    for ch in concatenated:
        all_chars.append(ch)



    for x,y in enumerate(concatenated):
        if x in positions:
            all_positions.append(1)
        else:
            all_positions.append(0)


    for place, cher in enumerate(all_chars):
        if cher == u"\u200C" and place + 1 < len(all_chars):
            all_positions[place + 1] = 2
            del all_chars[place]
            del all_positions[place]

    return list(zip(all_chars, all_positions))



def check_punc(char):
    punc = string.punctuation
    if char in punc:
        return "true"
    return "false"

def check_urdu_num(char):
    urnum = ['۱','۲','۳','۴','۵','۶','۷','۸','۹','۰']
    if char in urnum:
        return "true"
    return "false"

def check_greek(char):
    gre = ['α', 'β', 'γ', 'δ', 'Δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ξ', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ',
          'ω', 'Ω', 'Ψ', 'Φ', 'Σ', 'Π', 'Ξ', 'Γ']
    if char in gre:
        return "true"
    return "false"

def check_digit(char):
    digits = ['1','2','3','4','5','6','7','8','9','0']
    if char in digits:
        return "true"
    return "false"


def check_nonjoiner(char):
    nonjoiners = ['ا', 'د', 'ڈ', 'ز', 'ذ', 'ر', 'ڑ', 'ژ', 'و', 'ے']
    if char in nonjoiners:
        return "true"
    return "false"

def check_eng(char):
    eng = "[A-Za-z]"
    if char in eng:
        return "true"
    return "false"

def check_math(char):
    ma = ['≠', '≈', '≥', '≤', '⋅', '÷', '≅', 'π', '≜', ':=', '∝', '∞', '≪', '≫', '⌊', '⌋', '⌈', '⌉', 'σ2', '⊆', '⊂',
          '⊄', '⊇', '⊃', '⊅', '∈', '∉', '¬', '⇒', '⇔', '↔', '∀', '∃', '∄', '∫', '⋂', '⋃']
    if char in ma:
        return "true"
    return "false"



def create_feature_set(character, index):
    feature_set = [

        'current_character=' + character[index][0],
        'check_urdu_num=' + check_urdu_num(character[index][0]),
        'check_digit=' + check_digit(character[index][0]),
        'check_punc=' + check_punc(character[index][0]),
        'check_greek=' + check_greek(character[index][0]),
        'check_nonjoiner=' + check_nonjoiner(character[index][0]),
        'check_eng=' + check_eng(character[index][0]),
        'check_category=' + unicodedata.category(character[index][0]),
        'check_math=' + check_math(character[index][0]),
        'check_direction=' + unicodedata.bidirectional(character[index][0]),
    ]

    if index >= 1:
        feature_set.extend([
            'character[-1]=' + character[index - 1][0],
            'character[-1:0]=' + character[index - 1][0] + character[index][0],
        ])
    else:
        feature_set.append("start")

    if index >= 2:
        feature_set.extend([
            'character[-2]=' + character[index - 2][0],
            'character[-2:0]=' + character[index - 2][0] + character[index - 1][0] + character[index][0],
            'character[-2:-1]=' + character[index - 2][0] + character[index - 1][0],
        ])

    if index >= 3:
        feature_set.extend([
            'character[-3]=' + character[index - 3][0],
            'character[-3:0]=' + character[index - 3][0] + character[index - 2][0] + character[index - 1][0] + character[index][0],
            'character[-3:-1]=' + character[index - 3][0] + character[index - 2][0] + character[index - 1][0],
        ])

    if index >= 4:
        feature_set.extend([
            'character[-4]=' + character[index - 4][0],
            'character[-4:0]=' + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0] + character[index][0],
            'character[-4:-1]=' + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0],
        ])

    if index >= 5:
        feature_set.extend([
            'character[-5]=' + character[index - 5][0],
            'character[-5:0]=' + character[index - 5][0] + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0] + character[index][0],
            'character[-5:-1]=' + character[index - 5][0] + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0],
        ])

    if index >= 6:
        feature_set.extend([
            'character[-6]=' + character[index - 6][0],
            'character[-6:0]=' + character[index - 6][0] + character[index - 5][0] + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0] + character[index][0],
            'character[-6:-1]=' + character[index - 6][0] + character[index - 5][0] + character[index - 4][0] + character[index - 3][0] + character[index - 2][0] + character[index - 1][0],
        ])



    if index + 1 < len(character):
        feature_set.extend([
            'character[1]=' + character[index + 1][0],
            'character[0:1]=' + character[index][0] + character[index + 1][0],
        ])
    else:
        feature_set.append("start2")

    if index + 2 < len(character):
        feature_set.extend([
            'character[2]=' + character[index + 2][0],
            'character[0:2]=' + character[index][0] + character[index + 1][0] + character[index + 2][0],
            'character[1:2]=' + character[index + 1][0] + character[index + 2][0],
        ])

    if index + 3 < len(character):
        feature_set.extend([
            'character[3]=' + character[index + 3][0],
            'character[0:3]=' + character[index][0] + character[index + 1][0] + character[index + 2][0] + character[index + 3][0],
            'character[1:3]=' + character[index + 1][0] + character[index + 2][0] + character[index + 3][0],
        ])

    if index + 4 < len(character):
        feature_set.extend([
            'character[4]=' + character[index + 4][0],
            'character[0:4]=' + character[index][0] + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0],
            'character[1:4]=' + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0],
        ])

    if index + 5 < len(character):
        feature_set.extend([
            'character[5]=' + character[index + 5][0],
            'character[0:5]=' + character[index][0] + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0]  + character[index + 5][0],
            'character[1:5]=' + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0]  + character[index + 5][0],
        ])

    if index + 6 < len(character):
        feature_set.extend([
            'character[6]=' + character[index + 6][0],
            'character[0:6]=' + character[index][0] + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0]  + character[index + 5][0]  + character[index + 6][0],
            'character[1:6]=' + character[index + 1][0] + character[index + 2][0] + character[index + 3][0] + character[index + 4][0]  + character[index + 5][0]  + character[index + 6][0],
        ])

    return feature_set

processed_sentences_list = list()
for s in sentences:
    processed_sentences_list.append(sentence_making(s))


def all_feature_set(single_sentence):
    tempar = []
    for i in range(len(single_sentence)):
        tempar.append(create_feature_set(single_sentence, i))
    return tempar



def all_label_set(single_sentence):
    tempar = []
    for part in single_sentence:
        tempar.append(str(part[1]))
    return tempar


X_train = []
y_train = []
for rs in processed_sentences_list:
    X_train.append(all_feature_set(rs))

for rl in processed_sentences_list:
    y_train.append(all_label_set(rl))


model = pycrfsuite.Trainer(verbose=False)

for new_x, new_y in zip(X_train, y_train):
    model.append(new_x, new_y)

model.set_params({ 'c1': 1.0,   'c2': 1e-3, 'max_iterations': 500, 'feature.possible_transitions': True })


model.train('urdu-word-segmentation.crfsuite')


tag = pycrfsuite.Tagger()
tag.open('urdu-word-segmentation.crfsuite')

def tokenize(input_text):

    prediction = tag.tag(all_feature_set(input_text))
    lis = ""
    for x, y in enumerate(prediction):
        if y == "1":
            lis += " " + input_text[x]
        else:
            lis += input_text[x]
    return lis


print(tokenize("انسبحالتوںمیںہممختلفجذباتکےماتحتہوتےہیں"))

y_true = list()
y_pred = list()
for s in processed_sentences_list:
      prediction = tag.tag(all_feature_set(s))
      y_pred.extend(prediction)
      correct = all_label_set(s)
      y_true.extend(correct)

print(classification_report(y_true, y_pred))

print(confusion_matrix(y_true, y_pred))