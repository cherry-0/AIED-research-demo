import streamlit as st
import pandas as pd


st.header("1차시")

"### 활동 1. 사각형의 분류 복습하기"
"이번 시간에는 Algeomath(알지오매스) 도구를 활용하여 사각형의 분류를 복습해보겠습니다."
"아래 링크를 통해 알지오매스 페이지를 구경할 수 있습니다 :)"
st.link_button("알지오매스 페이지 구경하기", "https://www.algeomath.kr/algeomath/app/key/e4e6f79dfb6a11eda2b4f220ef6cc976/view.do")

st.link_button("🕹️**Algeomath 도구 사용법 설명 영상**", "https://drive.google.com/file/d/1oCAKVPR1vtN5iPx1HkgFWSi7rpE2HrHa/view?usp=drive_link")

"##### Algeo 문서 링크"
"아래 링크를 눌러 알지오 문서 페이지에 접속하세요."

"https://me2.do/5D3YsmD8"

"**진행방법 설명**"
st.success(
'''
1. 1-4페이지는 선생님과 친구들과 함께하는 페이지입니다. 수업에 집중해주세요! 빈칸은 선생님께서 시간을 정해주시면 채워주세요.
2. 5-7페이지에 주어진 사각형들을 주어진 도구들을 이용해 자유롭게 측정해보고, 측정 결과를 토대로 분류해주세요.
3. 분류 결과와 그렇게 생각한 이유를 아래 표에 채워주세요.
'''
)

df = pd.DataFrame(
    [
       {"apps": "https://drive.google.com/file/d/1HcCbbmC7Q17H5hNzp_0FCs9cjXrlpbuN/view?usp=drive_link", "name": "사각형 1", "분류 결과": "", "그렇게 분류한 이유": "", "정답 여부":""},
       {"apps": "https://drive.google.com/file/d/1caM_RmBZ_fhnlvwlixZ106aJ2oW7CjC1/view?usp=drive_link", "name": "사각형 2", "분류 결과": "", "그렇게 분류한 이유": "", "정답 여부":""},
       {"apps": "https://drive.google.com/file/d/1PUZ_M3FnTQLv30aAgIgBQMu6GerswNKa/view?usp=drive_link", "name": "사각형 3", "분류 결과": "", "그렇게 분류한 이유": "", "정답 여부":""},
       {"apps": "https://drive.google.com/file/d/1drrdyOzE1On2xVOIj2OK3PW7k2dxEHRp/view?usp=drive_link", "name": "사각형 4", "분류 결과": "", "그렇게 분류한 이유": "", "정답 여부":""},
   ]
)
edited_df = st.data_editor(df, 
                           column_config={
                               "apps": st.column_config.ImageColumn(
                                "미리보기 이미지(더블클릭해서 확인)", help="Streamlit app preview screenshots")
                           },
                           hide_index=True,
                           )

"표를 완성했다면 응답을 제출해 정답인지 확인해보세요."

if st.button("내 응답 제출하기"):
    df_csv = edited_df.to_csv("1차시_활동 1_응답.csv", index=False)
    #st.write(edited_df)
    edited_df['실제 분류'] = ["평행사변형", "평행사변형","정사각형", "평행사변형"]
    edited_df['정답 여부'] = (edited_df['분류 결과'] == edited_df['실제 분류']).apply(lambda x: 'O' if x else 'X')
    

st.write(edited_df[["apps", "name", "정답 여부"]])

st.text_area("내가 생각한 분류 결과와 실제 분류 결과가 일치하지 않은 사각형이 있었나요? 이유는 무엇이었나요?")




"### 활동 2. 블록코딩으로 사각형 이미지 데이터 만들기"

st.image("images/블록코딩배우기.png", use_column_width=True)

st.success('''
           이번 활동에서는 블록코딩을 이용해 사각형 이미지 데이터를 만들어보겠습니다. \n\n
           알지오 문서의 8페이지를 이용해 이미지를 자유롭게 제작해주세요.
           ''')

"내가 그린 사각형 중에 분류하기 어려울 만한 사각형 하나를 골라 그린 방법을 자유롭게 소개해 주세요."
col1, col2 = st.columns([0.4, 0.6])
with col1:
    uploaded_image = st.file_uploader("제작한 사각형 이미지 중 하나를 업로드해주세요.", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        st.image(uploaded_image, use_column_width=True)

with col2:
    text = st.text_area("사각형 이미지를 업로드한 후, 그린 방법을 소개해주세요")
    

if uploaded_image is not None and text != "":
    if st.button("내 응답 로컬에 저장하기"):
    
        with open("1차시_활동 2_응답.png", "wb") as f:
            f.write(uploaded_image.read())

        # Save the uploaded text
        with open("1차시_활동 2_응답.txt", "w") as f:
            f.write(text)
