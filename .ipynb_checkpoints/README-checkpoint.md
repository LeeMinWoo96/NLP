#### MRC QA 프로젝트(검역본부)를 위한 NLP 공부 및, BERT 자료정리

![](./img/flow.png)


---
기술 사용 사례
- 서울시 청년정책에선 유사도 측정에선 BM-25, MRC 경우 ETRI BERT를 사용
- 엑소브레인 법률상담 : MRC 부분에 자체 korBERT 모델 사용 
- 특허상담 논문 : bert + 한국어 임베딩 레이어 추가로 성능 향상을 보임을 증명

![](./img/good.png)


#### 참고자료

[KorSciQA: 한국어 논문의 기계독해 데이터셋 
](
http://semanticweb.kaist.ac.kr/home/images/b/b2/KorSciQA_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%85%BC%EB%AC%B8%EC%9D%98_%EA%B8%B0%EA%B3%84%EB%8F%85%ED%95%B4_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B.pdf)

[BERT를 이용한 한국어 특허상담 기계독해
](https://www.koreascience.or.kr/article/JAKO202013261020967.page)

[서울시 청년정책 질의응답
](https://medium.com/@ohikendoit/%EA%B8%B0%EA%B3%84%EB%8F%85%ED%95%B4%EB%A5%BC-%EC%9C%84%ED%95%9C-bert-%EC%96%B8%EC%96%B4%EC%B2%98%EB%A6%AC-%EB%AA%A8%EB%8D%B8-%ED%99%9C%EC%9A%A9-d1ea3a1fbc35)