## NLP
----

**자연어란?** 
- 우선 언어의 사전적인 의미는 생각, 느낌 따위를 나타내거나 전달하는 데에 쓰는 음성,문자 따위의 수단. 또는 그 음성이나 문자 따위의 사회 관습적인 체계

-> 자연어란 일반 사회에서 자연히 발생하여 쓰이는 언어

**자연어 처리란?**
- 컴퓨터를 이용하여 인간 언어의 이해, 생성 및 분석을 다루는 인공지능 기술

**기존 자연어 처리 접근**

1. Symbolic approach
- 규칙/지식 기반 접근법

2. Statistical approach
- 확률/통계 기반 접근법
- ex) TF-IDF


**자연어 처리 단계**

1. 전처리
- 불용어
- 공백
- 띄어쓰기

2. Tokenizing
- 어절
- 형태소
- n-grem
- WordPiece

3. Lexical analysis
- 어휘 분석
- 형태소 분석
- 개체명
- 상호참조

4. Syntactic analysis
- 구문 분석

5. Semantic analysis
- 의미 분석


---

**자연어 처리는 대부분 결국 분류 문제**

- 먼저 특징을 파악 후 특징을 바탕으로 그래프 위에 표현 후 경계를 나누어 분류 -> 과거에는 사람이 직접 분류 했었지만 **이젠 특징 파악과 분류를 컴퓨터가 하는 것이 기계학습의 핵심**


***그렇다면 어떻게 컴퓨터가 자연어를 좌표평면 위에 표현할까?***
- 가장 단순한 방식은 One-hot encoding 방식 -> Sparse representation
- 하지만 공간의 크기가 비효율적이고 단어가 가지는 **의미** 표현하기 어려움

이를 해결하기 위해 **Word2vec**

- 자연어의 의미를 백터 공간에 임베딩
- 한 단어의 주변 단어를 통해, 그 단어의 의미를 파악

주변부 단어를 예측하는 방식으로 학습(Skip-gram)

| Sparse representation | Dense representation |
|:--------:|:--------:|
| One-hot encoding | word embedding |
| n개의 단어에 대한 n차원의 벡터 | 한정된 차원의 밀집벡터 |
|의미 유추 불가능|의미 유추 가능|

- OOV(out of vocabulary) 에서 적용 불가능

**Fast text**
- 기존 원리는 word2vec과 유사하나 단어를 n-grem으로 나누어 학습을 수행
- 단어를 n으로 분리하여 학습 
- ex) ornage = 2-grem(O, Or, ra, an, ng, ge, e) -> 3-grem(Or,Ora,ran,ang,nge,ge) -> 4-grem(Ora,Oran,rang,ange,nge)-> 5-grem(Oran,Orang,range,ange)-> originam(Orange) **먄약 Oranges 가 들어왔다면 기존 Orange 와 유사한 ngrem이 많음 그래서 Oranges가 oov여도 유사한 거리의 벡터로 반환함**


- 만약 oov 일 경우, 입력단어의 n-grem vector들의 합산을 return 함


**활용예**
- 보통 가장 아랫단의 레이어로 사용

하지만 결국 동형어, 다의어 등에 대해선 성능이 좋지 못하다는 단점이 있음 -> ***문맥을 고려할 수 없음***

---

### 참고자료

[T 아카데미]()




