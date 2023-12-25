import streamlit as st
import os
import gdown
import zipfile
import pandas as pd 


st.header("2차시")


"### 활동 3. orange 소프트웨어 배우기" 

st.image("images/orange3intro.png", use_column_width=True)
         
st.link_button("🕹️**orange 소프트웨어 사용법 설명 영상**", "https://drive.google.com/file/d/1D9awgZg07msmaU6PHMdlQXIJ_ZwPLJ9J/view?usp=drive_link")

st.success(
'''
1. 아래 버튼을 눌러 orange 소프트웨어를 실행시켜 주세요. (새 창으로 열립니다.)
2. `OrangeTemplate.ows` 파일을 열어주세요. 혹은 위 그림을 보고 직접 여러 요소들을 배치해보세요. \n 위 영상을 참고해주세요.
'''
)
if st.button("🍊orange 소프트웨어 열기"):
      os.system("python -m Orange.canvas")
    
"다시 창을 닫고 돌아오셨나요? 그럼 다음 활동으로 넘어가주세요."

#"https://github.com/pragmatic-streamlit/streamlit-file-browser "
#뭔가 필요할 것 같음 

"----"
"#### 실험 1. 선생님이 준비한 데이터셋으로 분류 모델 훈련시키기"

"아래 버튼을 눌러 선생님이 준비한 데이터셋을 다운로드 받아주세요. (약 1분 소요)"
def download(url, filename, output_dir='.'):
      with st.spinner("Downloading {} ...".format(filename)):
            zip_file = os.path.join(output_dir, filename+".zip")
            gdown.download(url, zip_file, quiet=False)
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                  zip_ref.extractall(output_dir) 
            os.remove(zip_file)
        
      

if st.button("📁데이터셋 다운로드"):
      # Replace 'YOUR_GOOGLE_DRIVE_URL' with the actual shareable link for the zip file
      rectangle_url = "https://drive.google.com/drive/folders/1CW-dLLt8cKxvsmDk0MsCn1bahxtnvYq2?usp=drive_link"
      rhombus_url = "https://drive.google.com/drive/folders/12O0nX1Jy46pj8gIsb7IQuao7VTrAZgSF?usp=drive_link"
      square_url = "https://drive.google.com/drive/folders/1g062mElKTUcouLGVrsqrXFApEJmY2Sb3?usp=drive_link"
      download(rectangle_url, "rectangle")
      download(rhombus_url, "rhombus")
      download(square_url, "square")
      st.success("데이터셋 다운로드 완료!")
## TODO: 여기 이상함 - 다운로드 안됨 (bad zip...)

## TODO: 데이터셋 split 

if st.button("🍊orange 소프트웨어 열기", key="diff"):
      os.system("python -m Orange.canvas")
 
st.success("다운로드받은 데이터셋을 orange 에서 불러와 모델을 학습시켜 보세요. 결과를 보고 새로 알게 된 것이 있나요?")

with st.expander("궁금한 이미지 데이터 직접 확인하기"):
      st.write("원하는 파일 이름을 선택하면 아래에 이미지가 나타납니다.")
      #TODO: 이미지 데이터 직접 확인하기 위한 navigating code 
      
"---"
"#### 실험 2. 내가 만든 데이터셋으로 분류 모델 훈련시키기"

c1, c2, c3, c4 = st.columns(4)
with c1:
      st.button("직사각형 훈련 데이터 \n\n 추가하기", type="secondary", use_container_width=True)
      #TODO: upload -> save in local 
      
with c2:
      st.button("마름모 훈련 데이터 \n\n 추가하기", type="secondary", use_container_width=True)
      #TODO: upload -> save in local
with c3:
      st.button("직사각형 훈련 데이터 \n\n 제거하기", type="secondary", use_container_width=True)
      ## TODO: 가능하면 여러 개 동시에도 가능하게 
with c4:
      st.button("마름모 훈련 데이터 \n\n 제거하기", type="secondary", use_container_width=True)

st.success("데이터를 추가/제거할 때에는 orange 파일에서 데이터셋을 다시 불러와야 합니다.")

with st.expander("dataset 미리보기(test, train)"):
      #TODO: 1) selectbox 2)show images 
      st.write("데이터셋 미리보기")

#"https://github.com/jrieke/streamlit-image-select "

# import os
# import streamlit as st
# filelist=[]
# for root, dirs, files in os.walk("your folder directory"):
#       for file in files:
#              filename=os.path.join(root, file)
#              filelist.append(filename)
# st.write(filelist)

"##### 결과 기록지"

df = pd.DataFrame([{"시도 횟수":1, "전략":"", "정확도":0.7, "평가 결과":""}])
df_edit = st.data_editor(df, column_config={"시도 횟수":st.column_config.NumberColumn("시도 횟수"), "정확도":st.column_config.NumberColumn("정확도")}, hide_index=True)
with st.empty():
      st.write(df_edit)
if st.button("시도 기록 추가하기"):
      empty_row = {"시도 횟수":df_edit.shape[0], "전략":"", "정확도":0, "평가 결과":""}
      df_edit.loc[len(df_edit)] = empty_row
      #st.write(df_edit)
#### TODO: fix adding logic 

"---"

"### 아이디어 공유하기 "
st.success("아래 링크에 접속해 이번 시간을 통해 알아낸 좋은 전략에 대해 자랑해주세요")
" padlet/공유문서 링크 "

