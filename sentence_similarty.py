import pandas as pd
import numpy as np
import tqdm
tqdm.pandas()

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def similarity(text):
    sentence_A = train['text']
    sentence_B = train['bt_en_text']
    
    embedding_a = model.encode(sentence_A, convert_to_tensor = True)
    embedding_b = model.encode(sentence_B, convert_to_tensor = True)
    
    cosine_similarity = util.pytorch_cos_sim(embedding_a,embedding_b)
    
    return cosine_similarity.item()

train['similarity'] = train.progress_apply(similarity)

# Q1 이상인 text들
Q1 = np.percentile(train['similarity'],25)
over_Q1 = train.loc[train['similarity'] > Q1]