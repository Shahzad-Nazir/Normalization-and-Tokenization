# This Python file uses the following encoding: utf-8
import pandas as pd
import re
from unidecode import unidecode
import string
import difflib

import unicodedata

#------------------------------------Punctuation seperating function----------------------------------------------
def sep_punc(text_original):

    result = string.punctuation
    print(result)
    result=result.replace('.','')
    print(result)
    for x in result:

        if x in text_original:

            text_original = text_original.replace(x,x + " ")

    text_original = re.sub('\.(?!\s|\d|$)', ' . ', text_original)

    return text_original
#-------------------------------Punctuation seperating function Ended-----------------------------------------------

#---------------------------------space before and after symbols---------------------------------------------------

def sep_beforeandafter(text_original):
    ex = ['#','&','\\','(',')', '*', '+', '-','<','=','>', '@', '[',']','{','}','|','~']
    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " "+x+ " ")

    return text_original
#--------------------------------end space before and after-------------------------------

#------------------------------removing diacritics funtion------------------------------------------------------
def remove_dia(text_original):
    try:
        unichr
    except NameError:
        unichr = chr

    text_original = ''.join([t for t in text_original if t not in [unichr(x) for x in range(0x0600, 0x06ff) if unicodedata.category(unichr(x)) == "Mn"]])

    return text_original
#-----------------------------removing diacritics function ended---------------------------------------------------

#------------------------------Seperating Numbers funtion------------------------------------------------------
def sep_num(text_original):

    text_original = re.sub(r"([0-9]+(\.[0-9]+)?)", r" \1 ", text_original).strip()


    return text_original
#-----------------------------Seperating Numbers function ended---------------------------------------------------

#------------------------------Seperating Urdu Numbers funtion------------------------------------------------------
def sep_urdunum(text_original):

    text_original = re.sub(r"(['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']+(\.['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']+)?)", r" \1 ", text_original).strip()


    return text_original
#-----------------------------Seperating Urdu Numbers function ended---------------------------------------------------


#------------------------------Seperating English funtion------------------------------------------------------
def sep_eng(text_original):

    text_original = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", text_original)

    return text_original
#-----------------------------Seperating English function ended---------------------------------------------------


#------------------------------Replace standard funtion------------------------------------------------------
def rep_char(text_original):
    a1 = ['آ', 'أ', 'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
          'غ', 'ف', 'ق', 'ل', 'لا', 'م', 'ن', 'چ', 'ڈ', 'ڑ', 'ژ', 'ک', 'گ', 'ں',
          'و', 'ؤ', 'ھ', 'ہ', 'ۃ', 'ء', 'ی', 'ئ', 'ے']
    ar1 = [['ﺁ', 'ﺂ'], ['ﺃ'], ['ﺍ', 'ﺎ', ], ['ﺏ', 'ﺐ', 'ﺑ', 'ﺒ'], ['ﭖ', 'ﭘ', 'ﭙ', ], ['ﺕ', 'ﺖ', 'ﺗ', 'ﺘ'],
           ['ﭦ', 'ﭧ', 'ﭨ', 'ﭩ'], ['ﺛ', 'ﺜ', 'ﺚ'], ['ﺝ', 'ﺞ', 'ﺟ', 'ﺠ'],
           ['ﺡ', 'ﺣ', 'ﺤ', 'ﺢ'], ['ﺧ', 'ﺨ', 'ﺦ'], ['ﺩ', 'ﺪ'], ['ﺬ', 'ﺫ'], ['ﺭ', 'ﺮ'], ['ﺯ', 'ﺰ', ],
           ['ﺱ', 'ﺲ', 'ﺳ', 'ﺴ', ], ['ﺵ', 'ﺶ', 'ﺷ', 'ﺸ'], ['ﺹ', 'ﺺ', 'ﺻ', 'ﺼ', ],
           ['ﺽ', 'ﺾ', 'ﺿ', 'ﻀ'], ['ﻃ', 'ﻄ'], ['ﻅ', 'ﻇ', 'ﻈ'], ['ﻉ', 'ﻊ', 'ﻋ', 'ﻌ', ], ['ﻍ', 'ﻏ', 'ﻐ', ],
           ['ﻑ', 'ﻒ', 'ﻓ', 'ﻔ', ], ['ﻕ', 'ﻖ', 'ﻗ', 'ﻘ', ], ['ﻝ', 'ﻞ', 'ﻟ', 'ﻠ', ],
           ['ﻻ', 'ﻼ'], ['ﻡ', 'ﻢ', 'ﻣ', 'ﻤ', ], ['ﻥ', 'ﻦ', 'ﻧ', 'ﻨ', ], ['ﭺ', 'ﭻ', 'ﭼ', 'ﭽ'], ['ﮈ', 'ﮉ'], ['ﮍ', 'ﮌ'],
           ['ﮋ', ], ['ﮎ', 'ﮏ', 'ﮐ', 'ﮑ', 'ﻛ', 'ك'],
           ['ﮒ', 'ﮓ', 'ﮔ', 'ﮕ'], ['ﮞ', 'ﮟ'], ['ﻮ', 'ﻭ', 'ﻮ', ], ['ﺅ'], ['ﮪ', 'ﮬ', 'ﮭ', 'ﻬ', 'ﻫ', 'ﮫ'],
           ['ﻩ', 'ﮦ', 'ﻪ', 'ﮧ', 'ﮩ', 'ﮨ', 'ه', ], ['ة'], ['ﺀ'],
           ['ﯼ', 'ى', 'ﯽ', 'ﻰ', 'ﻱ', 'ﻲ', 'ﯾ', 'ﯿ', 'ي'], ['ﺋ', 'ﺌ', ], ['ﮮ', 'ﮯ', 'ﻳ', 'ﻴ', ]]

    a = 0
    for var in ar1:
        for x in var:
            text_original = text_original.replace(x, a1[a])

        a = a + 1

    return text_original
#-----------------------------Replace standard function ended---------------------------------------------------


#------------------------------Removing more than single white space funtion------------------------------------------------------
def rmv_spc(text_original):

    text_original = (re.sub("\s\s+", " ", text_original))

    return text_original
#-----------------------------Removing more than single white space function ended---------------------------------------------------

#------------------------------seperating Greek funtion------------------------------------------------------
def sep_greek(text_original):

    ex = ['α', 'β', 'γ', 'δ', 'Δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ξ', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ',
          'ω', 'Ω', 'Ψ', 'Φ', 'Σ', 'Π', 'Ξ', 'Γ']
    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original
#-----------------------------Seperating Greek function ended---------------------------------------------------

#------------------------------seperating Urdu ending funtion------------------------------------------------------
def sep_uend(text_original):

        ex = ['۔','،','؟','؛','٪']
        for x in ex:
            if x in text_original:
                text_original = text_original.replace(x, x + " ")

        return text_original
#-----------------------------Seperating urdu ending fuction ended---------------------------------------------------


#------------------------------seperating Math symbols funtion------------------------------------------------------
def sep_math(text_original):

    ex = ['≠', '≈', '≥', '≤', '⋅', '÷', '≅', 'π', '≜', ':=', '∝', '∞', '≪', '≫', '⌊', '⌋', '⌈', '⌉', 'σ2', '⊆', '⊂',
          '⊄', '⊇', '⊃', '⊅', '∈', '∉', '¬', '⇒', '⇔', '↔', '∀', '∃', '∄', '∫', '⋂', '⋃']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original
#-----------------------------Seperating Math symbols function ended---------------------------------------------------

#------------------------------seperating Urdu Poetry symbols funtion------------------------------------------------------
def sep_urdupoetic(text_original):


    ex = ['؎', '؃', '؏', '؂']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original
#-----------------------------Seperating Urdu Poetry function ended---------------------------------------------------


#------------------------------seperating Urdu Poetry symbols funtion------------------------------------------------------
def sep_urduquotessep(text_original):

    ex = ['\'', '“', '”', '‘', '’','"']

    for x in ex:
        if x in text_original:
            text_original = text_original.replace(x, " " + x + " ")

    return text_original
#-----------------------------Seperating Urdu Poetry function ended---------------------------------------------------

def urdu_normalizer(text_original):

    text = sep_punc(text_original)
    text = sep_beforeandafter(text)
    text = remove_dia(text)
    text = sep_num(text)
    text = sep_eng(text)
    text = rep_char(text)
    text = sep_greek(text)
    text = sep_math(text)
    text = sep_urdunum(text)
    text = sep_uend(text)
    text = sep_urduquotessep(text)
    text = sep_urdupoetic(text)
    text = rmv_spc(text)



    return text

#------------------------------Normalizer------------------------------------------------------------------------


#place text in original_text for normalization


original_text = "کراچی پاکستان میں موبائل ہینڈ سیٹس کے مینوفکچررز جون2020میں کابینہ سے منظور کی گئی موبائل ڈیوائس مینوفکچرنگ پالیسی کے تحت مقامی سطح پر اسمبلنگ کے مقصد کی طرف تیزی سے بڑھ رہے ہیںڈان اخبار کی رپورٹ کے مطابق اس سلسلے میں وزیر صنعت حماد اظہر سے موبائل کمپنی ویوو کے نمائندوں نے ملاقات کی جس کے بعد انہوں نے سوشل میڈیا پلیٹ فارم ٹوئٹر پر اپنے اکانٹ سے یہ اعلان کیا کہ کمپنی نے پاکستان میں اسمارٹ فون تیار کرنے کی سہولت قائم کرنے کا فیصلہ کیا ہے اور اس منصوبے کے لیے زمین خرید لی گئی ہےمزید پڑھیں موبائل فون کی مینوفیکچرنگ پالیسی منظورتاہم ویوو کے نمائندوں کی جانب سے اس ملاقات پر ردعمل دینے سے گریز کیا گیاخیال رہے کہ جون 2020 میں وفاقی کابینہ نے پالیسی منظور کی تھی لیکن انڈسٹری کے کچھ کھلاڑیوں نے کہا ہے کہ اس میں بہت سے خدشات ہیںاس پس منظر میں ڈان سے گفتگو میں ان کا کہنا تھا کہ پالیسی میں لوکلائزیشن کی شرط کو پاکستان میں نافذ کرنا ناممکن ہے کیونکہ اسکرینز مدربورڈز اور بیٹریز کی تیاری یہاں ممکن نہیں ہےپالیسی میں موبائل ڈیوائسز کی سی کے ڈیایس کے ڈی مینوفکچرنگ پر فکسڈ سیلز ٹیکس کے خاتمے کی یقین دہانی کے ساتھ ساتھ مقامی سطح پر اسمبلڈ ڈیوائسز کی مقامی فروخت پر فیصد ود ہولڈنگ ٹیکس سے استثنی بھی شامل ہے تاہم انڈسٹری پلیئرز کہتے ہیں کہ ان اقدامات پر عمل درامد ابھی تک مکمل نہیں ہوااس صنعت کے ایک اندرونی پلیئر نے نام ظاہر نہ کرنے کی شرط پر اس لیے ڈان کو بتایا چونکہ حکومت کے ساتھ بات چیت ابھی جاری ہےیہ بھی پڑھیں مالی سال 2020 ملک میں موبائل فون کی درامد پر 54 ارب روپے کی ڈیوٹی وصولانہوں نے کہا کہ ان 'استثنی کے بغیر مقامی ?اسمبلی ممکن نہیں $ہےجون %میں پالیسی کی کابینہ کیKashifمنظوری کے بعد وزارت کی جانب سے جاری اعلامیے میں کہا گیا تھا کہ ملک میں کل 16 مقامی کمپنیاں موبائل لات تیار کررہی ہیں جن میں سے بیشتر کمپنیاں فیچر فون یعنی جی تیار کررہی ہیں کمپنیاں اب اسمارٹ فون تیار کرنے کی طرف جارہی ہیں کیونکہ ٹیکنالوجی جی جی کی طرف منتقل ہو رہی ہےٹیلی کام کے ایگزیکٹوز نے ڈان کو بتایا کہ جی قابل ہینڈ سیٹس کی کمی پاکستان کی ڈیجیٹل ترقی کی راہ میں سب سے بڑی رکاوٹ ہے ملک میں ڈیجیٹل انقلاب کو فروغ دینے کے لیے ان ہینڈسیٹ کی مقامی اسمبلی ناگزیر ہےگزشتہ مالی سال 2020 میں موبائل ہینڈسیٹس کی درمدات تیزی سے بڑھ کر ایک ارب 37 کروڑ ڈالر تک جا پہنچی تھی جبکہ مالی سال 2021 کے جولائی سے ستمبر کے درمیان یہ 49کروڑ20لاکھ ڈالرز کو عبور کرچکی,ہیں اور سست ہوتی معیشت\کے باوجودALI AHMADگزذشتہ@سا۲۲۲ل کے۲,ریکارڈ*??&&/>,<\|()[{#@%^&*_-+=~``≠کوπمات دیﻨے کے∞لیے تیار ہیں اِس-اُس"
#
print(original_text)

text = urdu_normalizer(original_text)

print(text)
