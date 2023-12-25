import streamlit as st
st.title("2차시")


"### orange 소프트웨어 배우기" 
"#### 사진"
"#### 참고 영상 "

"### orange 열기 버튼"


"### orange file open"

"https://github.com/pragmatic-streamlit/streamlit-file-browser "
#뭔가 필요할 것 같음 

"### 기존 dataset orange에서 접근 "

"1. 방법 1: gdown"
"2. 방법 2: 첨부된 폴더 사용"

"### dataset의 이미지 미리보기 할 수 있게 (test, train)"

"https://github.com/jrieke/streamlit-image-select "

import os
import streamlit as st
filelist=[]
for root, dirs, files in os.walk("your folder directory"):
      for file in files:
             filename=os.path.join(root, file)
             filelist.append(filename)
st.write(filelist)


"### 새로운 data 를 기존 dataset에 넣기 / 빼기 (이부분이 가장 어려울듯)"
"multi select -> button -> add"
"multi select -> button -> remove"

"### 결과 기록지"

"표"

"### 아이디어 공유: padlet/공유문서 링크 "
"##### (공유문서에는 예시 1-2개 넣기)"
