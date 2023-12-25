import streamlit as st
st.header("3차시")

"### 활동 4. 새로운 테스트 데이터셋을 분류해 보기"
st.success("선생님과 함께 새로운 데이터셋으로 인공지능 멘티를 학습시켜본 후에 답해봅시다.")

if st.button("새로운 데이터셋 다운로드"):
    pass #TODO

"orange 창을 닫았다면 다시 열어주세요!"
if st.button("🍊orange 소프트웨어 열기"):
      os.system("python -m Orange.canvas")
    
st.text_area("현재 인공지능 멘티가 잘못 분류하는 이미지는 어떤 이미지인가요 잘 분류하지 못하는 이유는 무엇일까요? ", height=300)

st.success("현재 인공지능 멘티가 사각형 이미지를 더 정확하게 분류하도록 하기 위해서는 데이터셋을 어떻게 구성해야 할까요 데이터셋을 수정한 후 다시 학습시켜봅시다.")
"###### 훈련 데이터셋 수정하기"
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

st.text_area("결과를 자유롭게 정리해 봅시다.", height=300)

"---"

"#### 내 결과물 공유하기 "

" 1. 분류결과 캡처"
" 2. 분석"
" 3. 내 훈련 데이터셋"
#TODO
st.button("분류결과 스크린샷 업로드")
st.button("내 훈련 데이터셋 압축하기")



st.success("결과가 쉽게 나아지지 않더라도 그것은 이상한 일이 아닙니다. 그것은 사각형을 우리가 분류하는 방식과 인공지능 모델이 분류하는 방법이 정말 다르기 때문입니다. ")
with st.expander("자세한 설명 확인하기"):
    st.write('''분류 모델에는 크게 두 가지 유형이 있습니다:  

이진 분류 모델: 이 모델은 '예' 또는 '아니오'와 같이 두 가지 선택지 중 하나를 선택할 수 있습니다. 마치 컴퓨터에게 '이것이 원이 맞아?' 물어보는 것과 비슷합니다. 컴퓨터는 두 가지 옵션 사이에서 결정을 내리게 됩니다.

예시: 이 모양이 원인가요? (예 또는 아니오)

다중 분류 모델: 이 모델은 여러 가지를 인식하고 이름을 붙일 수 있는 전문가와 같습니다. 두 개 이상의 카테고리를 다룰 수 있습니다. 예를 들면 이 모양이 원, 사각형 또는 마름모 중 어떤 것인지를 말할 수 있습니다.

예시: 이 모양은 어떤 종류인가요? (원, 사각형 또는 마름모)

그러나 이 모델들은 카테고리 간에 서로 겹치는 경우에는 잘 작동하지 않을 수 있습니다. 예를 들어 직사각형과 마름모처럼 일부 속성을 공유하는 모양들을 구별하도록 컴퓨터에게 가르치려면 어려울 수 있습니다. 이 모양들은 '직사각형 모양의 마름모' 또는 '마름모 모양의 직사각형'과 같이 보일 수 있어서 컴퓨터에게 판단하기 어려울 수 있습니다.

분류 모델은 강력하지만 때로는 어려운 경우가 있으며, 특히 카테고리가 서로 겹칠 때에는 한계가 있을 수 있습니다. 마치 똑똑한 컴퓨터에게 복잡한 모양들을 구분하라고 부탁하는 것과 비슷합니다. 심지어 가장 똑똑한 컴퓨터라도 이런 경우에는 퍼즐처럼 어려울 수 있습니다!''')


# "### option:"
# "내가 작성한 결과물 pdf로 출력"

