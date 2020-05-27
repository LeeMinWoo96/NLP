
### 언어 모델

- 모델: 대상 주제를 도면이나 사진 화상을 사용하거나 수식 등을 사용하여 표현한 것

**자연어의 법칙을 컴퓨터로 모사한 모델 -> 언어 모델**

---



1. Makov 확률 기반의 언어 모델
- 가장 기초 언어모델 , 다음 단어나 문장이 나올 확률을 통계와 단어의 n-grem 기반으로 계산

2. RNN 기반의 언어 모델
- RNN읜 히든 노드가 방향을 가진 엣지로 연결돼 순환 구조를 이루는 신경망
- 이전 state가 다음 state까지 영향을 미치므로 시계열 데이터 처리에 특화
- Seq2seq 
  - 입력이 순차적으로 들어가고 출력 또한 순차적으로 들어갇나
  - Encoder(context vector) - Decoder(획든 context vector를 입력으로 다음 state 예측)
  
- 단점
  - 가중치 소실
  - 모든 token이 영향을 미치니 , 중요하지 않은 token도 영향을 줌
  

3. Attention 모델
- 인간이 정보처리를 할 때 모든 sequence를 고려하는 것은 아님 -> 즉 집중해야하는 것을 고려하자 라는 것이 모티브

![](./img/attention.png)

- 기존 Seq2Seq 에선 RNN의 최종 output인 Context vector만 활용
- Attention에서는 인코더의 RNN 셀의 각각 output을 활용
- Decoder 에서는 매 step 마다 RNN 셀의 output을 이용해 dynamic하게 context vector 생성

*Decoder 결과가 다르면 역전파 과정을 통해 attention 수정*

**-> 어쨋든 RNN이 순차적으로 연산이 이뤄짐에 따라 연산 속도가 느림**

4. Self-attention 모델
- Attention in all you need!
![](./img/sa1.png)
![](./img/sa2.png)
![](./img/sa3.png)

--- 
**BERT에는 Mult-head self attention 원리 사용**
- Self attention을 여러개를 동시에 사용하는 것
- GPU 에선 행렬 곱에대한 병렬처리가 가능함 따라서 gpu에서 더 효율적
- bert에선 12개의 self attention

***버트는 Mult-head attention으로 이루어진 encoder를 여러층 쌓아서 encoding을 수행 -> transformer 모델***



---

### BERT

- transformer 의 encoder 만 사용
- WordPiece tokenizing

1. WordPiece tokenizing
- Byte Pair Encoding 알고리즘 이용
- 빈도수에 기반에 단어를 의미 있는 패턴(subword)로 잘라서 tokenizing


![](./img/wpt.png)


![](./img/wp2.png)

![](./img/wpt3.png)


![](./img/wpt4.png)



2. input

- 앞은 cls 뒤엔 sep 토큰을 붙임 그 후 15% 확률로 임의의 토큰을 고름 거기서 80%은 Mask 10%는 랜덤단어 나머지는 안바꿈. 
- Mask가 뭔지와 문장 사이의 관계(is next, not next)를 학습함

token Embedding : word

segment embedding : 문장이 a인지 b인지

postion embedding : 순서에대해 학습을 위해 토큰 위치

를 거침



  

max seq_length 는 입력 시퀀스들어갈때 ab가 합쳐졌을때 길이가 몇인지(토큰 기준)
실제 preprocess data 
preprocess 할때 mask 화 tokenizing 하고 진행





