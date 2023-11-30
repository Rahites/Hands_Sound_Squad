# Hand_Sound_Squad

**2023 6th D&A BigData Conference**  
Team : 수어 사운드 스쿼드

## 주제
**한국 농인을 위한 수어 통역 시스템 구축**  
수어 통역 시스템을 구축하여 한국 청각/언어 장애인의 의사소통을 지원하자!

## Task Flow
1. Video Input
2. Pose Estimation
- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
3. Preprocessing
- KeyPoint Preprocessing  
- [Normalize Method Reference](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11195549&nodeId=NODE11195549&medaTypeCode=185005&locale=ko&foreignIpYn=N&articleTitle=Openpose%EC%99%80+GRU+%EA%B2%B0%ED%95%A9%EC%9D%84+%ED%99%9C%EC%9A%A9%ED%95%9C+%EC%88%98%EC%96%B4+%EB%8B%A8%EC%96%B4+%EC%9D%B8%EC%8B%9D&articleTitleEn=Sign-Language+Word+Recognition+Using+Combination+of+Openpose+and+GRU&language=ko_KR&hasTopBanner=true)

4. Modeling  
- Bi-LSTM + Attention
<img src="Modeling/Architecture.png">

5. Predict Answer Words(UI)
- Model Inference
6. Predict Korean postpositions(UI)
- Use [KLUE-BERT base](https://huggingface.co/klue/bert-base)
- Make Sentence
7. TTS(UI)
- Use [gTTS](https://pypi.org/project/gTTS/)