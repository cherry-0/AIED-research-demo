import streamlit as st 
import os
from st_pages import Page, show_pages

with st.spinner("Loading pages..."):
    show_pages(
        [
            Page("intro.py", "Introduction", "🏠"),
            Page("pages/1차시.py", "1차시", ":one:"),
            Page("pages/2차시.py", "2차시", ":two:"),
            Page("pages/3차시.py", "3차시", ":three:")
        ]
    )

st.title("AIED Research 2023 demo page")

st.success("2023 AIED 장기프로젝트 최종결과물 체험을 위한 페이지입니다. \n\n 연구 소개를 위한 게시글 링크는 https://aiednet.kr/sub_posting/posting_view.php?number=306&dp1=competition&cu_page=https://aiednet.kr/sub_competition/research.php 입니다.")



    

"### 1. 개요"

"페이지의 안내를 따라가면 수업안의 전체 구성을 경험해 볼 수 있습니다."

"수업안의 구성 근거 및 자세한 소개는 원 게시글의 첨부 파일들을 참고해 주세요 😀"

"##### 제공되는 파일"

"* 수업안 전체 구성 및 구성근거 소개 보고서(pdf)"
"* 수업안 전체 구성 및 구성근거 소개 영상(YouTube)"



"### 2. 교사용 가이드라인 링크(Notion)"

"https://sugared-pocket-191.notion.site/43d0dd315cf0454489f2415ce821a9f0?pvs=4 "


