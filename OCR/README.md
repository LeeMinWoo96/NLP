### OCR (kakao, naver, ABBYY fileReader) 비교 및 사용예

#### OCR(광학 문자 인식) 이란? 
- 광학 문자 인식은 사람이 쓰거나 기계로 인쇄한 문자의 영상을 이미지 스캐너로 획득하여 기계가 읽을 수 있는 문자로 변환하는 것이다.

영어의 경우 오픈소스 (테서렉트) 등으로 충분히 인식이 잘되지만 한국어나 일본어의 경우는 인식률이 좋지 않다.


PDF -> TXT 변환을 하기 위해 OCR을 사용해본다. (PDF가 image로 이뤄진 경우가 많기 때문에 그냥 pdf2txt로는 추출 x)


----
[naverApi 코드](./naverTest.py)

[kakaoApi 코드](./KakaoTest.py)

[pdf2txt 코드](./pdf2txt.py)

[pdf2image 코드](./pdftoimage.py)

[tika 코드](./tika_sample.py)