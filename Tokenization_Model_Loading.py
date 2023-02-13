# This Python file uses the following encoding: utf-8

import re
import codecs
import string
import unicodedata
import pycrfsuite

def sep_punc(text_original):

    result = string.punctuation
    result=result.replace('.','')

    for x in result:

        if x in text_original:

            text_original = text_original.replace(x,x + " ")

    text_original = re.sub('\.(?!\s|\d|$)', ' . ', text_original)

    return text_original




def sep_beforeandafter(text_original):
    ex = ['#','&','\\','(',')', '*', '+', '-','<','=','>', '@', '[',']','{','}','|','~']
    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " "+x+ " ")

    return text_original


def sep_num(text_original):

    text_original = re.sub(r"([0-9]+(\.[0-9]+)?)", r" \1 ", text_original).strip()


    return text_original



def sep_urdunum(text_original):

    text_original = re.sub(r"(['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']+(\.['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']+)?)", r" \1 ", text_original).strip()


    return text_original




def sep_eng(text_original):

    text_original = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", text_original)

    return text_original




def sep_greek(text_original):

    ex = ['α', 'β', 'γ', 'δ', 'Δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ξ', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ',
          'ω', 'Ω', 'Ψ', 'Φ', 'Σ', 'Π', 'Ξ', 'Γ']
    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original


def sep_uend(text_original):

    ex = ['۔','،','؟','؛','٪']
    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, x + " ")

    return text_original



def sep_math(text_original):

    ex = ['≠', '≈', '≥', '≤', '⋅', '÷', '≅', 'π', '≜', ':=', '∝', '∞', '≪', '≫', '⌊', '⌋', '⌈', '⌉', 'σ2', '⊆', '⊂',
          '⊄', '⊇', '⊃', '⊅', '∈', '∉', '¬', '⇒', '⇔', '↔', '∀', '∃', '∄', '∫', '⋂', '⋃']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original



def sep_urdupoetic(text_original):


    ex = ['؎', '؃', '؏', '؂']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original



def sep_urduquotessep(text_original):

    ex = ['\'', '“', '”', '‘', '’','"']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original



def rmv_spc(text_original):

    text_original = (re.sub("\s\s+", " ", text_original))

    return text_original

def seperator(text_original):
    text = sep_punc(text_original)
    text = sep_beforeandafter(text)
    text = sep_num(text)
    text = sep_eng(text)
    text = sep_greek(text)
    text = sep_math(text)
    text = sep_urdunum(text)
    text = sep_uend(text)
    text = sep_urduquotessep(text)
    text = sep_urdupoetic(text)
    text = rmv_spc(text)
    return text






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


def all_feature_set(single_sentence):
    tempar = []
    for i in range(len(single_sentence)):
        tempar.append(create_feature_set(single_sentence, i))
    return tempar




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
    return seperator(lis)


print(tokenize("انسبحالتوںمیںہممختلفجذبات@کےماتحتہوتےہیں"))