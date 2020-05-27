## BERT

### BERT 란?
- 사전 훈련 언어모델
-> 대량의 코퍼스를 Encoder가 임베딩하고, 이를 전이하여 파인튜닝해 task를 수행한다.

----

![bert](./img/bert.png)

현재 korQuard 데이터셋으로 진행되는 QA 대회에서 보통 BERT가 상위권을 점유하고 있다.


BERT를 이해하려면 트랜스포머의 개념을 이해해야하는데 관련 내용은 아래 링크에 들어가서 확인할 수 있다.


[트랜스포머](https://wikidocs.net/31379)

-----

#### BERT 의 Input

Token Embedding + Segment Embedding + Postion Embedding 으로 진행된다.


**Token Embedding**
- word Piece 임베딩 방식, [참고](https://lovit.github.io/nlp/2018/04/02/wpm/)

**Segment Embedding**
- 토큰 시킨 단어를 다시 하나의 문장으로 만드는 작업, Bert에서는 두개의 문장을 구분자를 넣어 구분하고 두 문장을 하나의 Segment로 지정하여 입력함

**Postion Embedding**
- 여기서 TransFormer의 개념이 들어가는데 BERT는 Transformer의 인코더, 디코더 중 인코더만 사용함, Self Attention은 입력의 위치를 고려하지 않고 입력 토큰의 위치 정보를 고려, 즉 Postion Encoding은 Token 순서대로 인코딩을 하는 것을 뜻합니다.

---

#### BERT의 Pre-training
- MLM(Masked Language Model)
- NSP(Next Sentence Prediction)
위 두가지 방식을 사용 *논문에서는 MLM 방식이 더 좋은 성능을 보임*

**MLM**
- 입력 문장에서 임의의 토큰을 Mask 처리하고 그 토큰을 맞추는 방식

**NSP**
- 두 문장이 주어졌을때 두 문장의 순서를 맞추는 방식, 문장간의 관련성이 중요한 NLI, QA의 파인튜닝을 위해 문장 간의 연관을 맞추는 학습 

***그래서 보통 두가지를 다 적용한 것이 뛰어난 성능을 보입니다.***


---

#### BERT의 Transfer Learning

학습된 언어모델을 전이학습 시켜 실제 Task 를 수행하는 과정
-> 기존에는 해당 주제 (QA, NER)등을 풀고 싶다하면 그에따라 모델을 따로 구성해야했다. 하지만 BERT는 사전 훈련된 언어모델을 사용하여 전이학습시켜 원하는 주제에 관한 모델로 활용할 수 있다.

BERT위 pre-train은 준지도 학습으로 진행하지만 전이학습은 지도학습으로 진행된다.



----
#### 참고자료 

[https://ebbnflow.tistory.com/151](https://ebbnflow.tistory.com/151)