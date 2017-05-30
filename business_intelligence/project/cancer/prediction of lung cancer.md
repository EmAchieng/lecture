# CT사진을 이용한 폐암예측


### 12주차 진행 사항(5/23)
- <b>페이지 생성</b><br></br>
<img src="https://github.com/SeongCheol-Kim/prediction_of_lung_cancer/blob/master/example_pic/%ED%99%88.png?raw=true" width="400" height="250" align="middle"></img>
<br></br>
<img src="https://github.com/SeongCheol-Kim/prediction_of_lung_cancer/blob/master/example_pic/%ED%8C%90%EC%A0%951.png?raw=true" width="400" height="250" align="middle"></img>
<br></br>
<img src="https://github.com/SeongCheol-Kim/prediction_of_lung_cancer/blob/master/example_pic/%ED%8C%90%EC%A0%952.png?raw=true" width="400" height="250" align="middle"></img>
<br></br>
- <b>데이터 전처리</b><br></br>
    * 총 데이터(1595개)중 라벨링이 존재하지 않는 데이터 제거 -> 최종 학습데이터(1397개)<br></br>
        -> 라벨링이 존재하지 않는 데이터(198개)는 테스트 데이터로 활용 예정
    * dicom형태의 파일을 numpy로 변환
    * 사진 사이즈 변환(1장당 150 * 150 * 20)
- <b>성능</b><br></br>
    * Cross validation -> 8 : 2 
    * Accuracy : 약 69%
<br><br>    
### 13주차 진행 사항(5/30)
- <b>페이지 개선</b><br>
   * 메인 페이지
   <img src="https://github.com/jayoungseo/quiz-image/blob/master/home.png?raw=true" align="middle"></img>
- <b>성능 향상</b>
   * Accuracy : 약 69% --> 73%
