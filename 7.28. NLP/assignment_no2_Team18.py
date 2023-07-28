import pandas as pd
from tqdm import tqdm
from konlpy.tag import Okt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Raw 데이터 전처리
df = pd.read_csv('./shopping.txt', sep='\t')
df.columns = ['rating', 'review']
df.index = df.index+1
df['rating'] = df['rating'].replace([1,2,4,5], [0,0,1,1])
df.drop_duplicates(subset=['review'], inplace=True)

ydata = df['rating']
xdata = df['review']

# 학습/테스트 셋 분리
xtrain, xtest, ytrain, ytest = train_test_split(xdata, ydata, test_size=0.3, random_state=902, stratify=ydata)

# 불용어 정의
stopwords = []
with open('./stopwords.txt', 'r') as f:
    for line in f:
        line = line.strip()
        stopwords.append(line)
f.close()

# 불용어 제거
okt = Okt()
x_train = []
for sentence in tqdm(xtrain):
    sentence = okt.morphs(sentence, stem=True)  # 토큰화
    stopwords_removed_sentence = [word for word in sentence if not word in stopwords]  # 불용어 제거
    x_train.append(stopwords_removed_sentence)

x_test = []
for sentence in tqdm(xtest):
    sentence = okt.morphs(sentence, stem=True)  # 토큰화
    stopwords_removed_sentence = [word for word in sentence if not word in stopwords]  # 불용어 제거
    x_test.append(stopwords_removed_sentence)

# 전처리 (워드 임베딩, 패딩, etc..)
tok=Tokenizer()
tok.fit_on_texts(xdata)
xtrain_enc=tok.texts_to_sequences(x_train)

w2i = tok.word_index

maxLen = max(map(len, xtrain_enc))
xtrain_padded = pad_sequences(xtrain_enc, maxlen=maxLen)
vocab_size = len(w2i)+1

# 모델링
model = Sequential()
model.add(Embedding(vocab_size, 32))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(xtrain_padded, ytrain, epochs=5, batch_size=32, validation_split=0.3)

xtest_enc = tok.texts_to_sequences(x_test)
xtest_padded = pad_sequences(xtest_enc, maxlen=maxLen)
print(model.evaluate(xtest_padded, ytest))


