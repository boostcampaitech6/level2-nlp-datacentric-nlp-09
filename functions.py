import numpy as np
import pandas as pd
import random
import pickle
import re
from tqdm import tqdm
tqdm.pandas()

from transformers import AutoModelForSequenceClassification, AutoTokenizer


# checking UNK token
model_name = 'klue/bert-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)

def text_tokenizer(text):
  input_ids = tokenizer.encode(text)
  result = tokenizer.decode(input_ids)
  if '[UNK]' in result:
    return True
  else:
    return False

train['unk_checking'] = train['text'].progress_apply(lambda x: text_tokenizer(x))

##### EDA ######
# change synonym 
path = "user-path"
wordnet = {}
with open(path,"rb") as f:
  wordnet = pickle.load(f)
  
def get_only_hangul(line):
  parseText = re.compile('/ ^[ㄱ-ㅎㅏ-ㅣ가-힣]*$/').sub('',line)
  return parseText

def synonym_replacement(words,n):
  new_words = words.copy()
  random_word_list = list(set([word for word in words]))
  random.shuffle(random_word_list)
  num_replaced = 0
  for random_word in random_word_list:
    synonyms = get_synonyms(random_word)
    if len(synonyms) >= 1:
      synonym = random.choice(list(synonyms))
      new_words = [synonym if word == random_word else word for word in new_words]
      num_replaced += 1
    if num_replaced >= n:
      break

  if len(new_words) != 0:
    sentence = ' '.join(new_words)
    new_words = sentence.split(" ")

  else:
    new_words = ""

  return new_words

def get_synonyms(word):
  synonyms = []

  try:
    for syn in wordnet[word]:
      for s in syn:
        synonyms.append(s)
  except:
    pass

  return synonyms

# randomly deletion
def random_deletion(words,p):
  if len(words) == 1:
    return words

  new_words = []
  for word in words:
    r = random.uniform(0,1)
    if r > p:
      new_words.append(word)

  if len(new_words) == 0:
    rand_int = random.randint(0,len(words) - 1)
    return [words[raind_int]]