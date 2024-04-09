# 🏝 멤버 구성 및 역할

| [전현욱](https://github.com/gusdnr122997) | [곽수연](https://github.com/gongree) | [김가영](https://github.com/garongkim) | [김신우](https://github.com/kimsw9703) | [안윤주](https://github.com/nyunzoo) |
| --- | --- | --- | --- | --- |
| <img src="https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-01/assets/81287077/0a2cc555-e3fc-4fb1-9c05-4c99038603b3)" width="140px" height="140px" title="Hyunwook Jeon" /> | <img src="https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-01/assets/81287077/d500e824-f86d-4e72-ba59-a21337e6b5a3)" width="140px" height="140px" title="Suyeon Kwak" /> | <img src="https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-01/assets/81287077/0fb3496e-d789-4368-bbac-784aeac06c89)" width="140px" height="140px" title="Gayoung Kim" /> | <img src="https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-01/assets/81287077/77b3a062-9199-4d87-8f6e-70ecf42a1df3)" width="140px" height="140px" title="Shinwoo Kim" /> | <img src="https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-01/assets/81287077/f3b42c80-7b82-4fa1-923f-0f11945570e6)" width="140px" height="140px" title="Yunju An" /> |
- **전현욱**
    - 팀 리더, Label Error Detection, G2P Noise
- **곽수연**
    - 특수문자 및 한자 처리, Back Translation
- **김가영**
    - Semantic Similarity Analysis
- **김신우**
    - Data Augmentation
- **안윤주**
    - Text Keyword Extraction

# 🍍 프로젝트 기간

2024.01.24 10:00 ~ 2024.02.01 19:00


# 🍌 프로젝트 소개

- 자연어에서 독해 및 분석 과정을 거쳐 주어진 태스크를 수행하기 위해서는 자연어의 주제에 대한 이해가 필수적이다. KLUE-Topic Classification benchmark는 뉴스의 헤드라인을 통해 그 뉴스가 어떤 topic을 갖는지를 분류해 내는 task로, 각 자연어 데이터에서 생활문화, 스포츠, 세계, 정치, 경제, IT과학, 사회 등 다양한 주제 중 하나로 라벨링한다. 
- 본 프로젝트는 Data-Centric의 목적에 맞게 주어진 데이터셋을 바탕으로 베이스라인 모델의 수정 없이 오로지 데이터의 수정으로만 성능 향상을 이끌어내야 한다.

# 🥥 프로젝트 구조

- Train Data : 7,000개
- Test Data : 47,785개

## 데이터셋 구조

| Column | 설명 |
| --- | --- |
| ID | 데이터 샘플의 고유번호 |
| text | 분류의 대상이 되는 연합 뉴스 기사의 헤드라인. 한국어 텍스트에 일부 영어, 한자 등의 단어가 포함 |
| target | 정수로 인코딩된 라벨 |
| url | 데이터 샘플의 뉴스 url (출처) |
| date | 데이터 샘플의 뉴스가 작성된 날짜와 시간 |

## Label Class 기준

| id | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 설명 | IT과학 | 경제 | 사회 | 생활문화 | 세계 | 스포츠 | 정치 |


## 평가 지표
- **macro F1 score** : 모든 class f1 score의 평균
- accuracy

# 🤿 사용 모델

- klue/bert-base (고정)

# 👒 폴더 구조

```bash
.
|-- README.md
|-- Special_character_check.ipynb
|-- back_translation.ipynb
|-- category_per_cnt.ipynb
|-- category_word_add.ipynb
|-- data
|   |-- culture.txt
|   |-- economy.txt
|   |-- it_science.txt
|   |-- politics.txt
|   |-- society.txt
|   |-- sport.txt
|   |-- train_special_characters.csv
|   `-- world.txt
|-- error_detection.ipynb
|-- functions.py
|-- g2pk.ipynb
|-- hanja.ipynb
|-- kmeans.ipynb
|-- sentence_similarty.py
|-- special_character.ipynb
`-- wrap-up_report.pdf
```

# 🍸 Leaderboard

|  |  f1 | accuracy |
| --- | --- | --- |
| Public | 0.8454 | 0.8484 |
| Private | 0.8414 | 0.8443 |
