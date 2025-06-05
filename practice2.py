# multi_page_app.py
import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# Home Page
# -------------------------
class HomePage:
    def __init__(self):
        st.title("🏠 Home Page")
        st.write("이 앱은 `st.Page` 구조로 만들어진 멀티페이지 앱입니다.")
        st.markdown("탭이 아닌 **URL 라우팅 기반** 페이지 전환 방식입니다.")


# -------------------------
# Data Page
# -------------------------
class DataPage:
    def __init__(self):
        st.title("📊 데이터 페이지")
        df = pd.DataFrame({
            "이름": ["Alice", "Bob", "Charlie", "David"],
            "점수": [85, 90, 78, 92]
        })
        st.write("샘플 데이터:")
        st.dataframe(df)


# -------------------------
# Chart Page
# -------------------------
class ChartPage:
    def __init__(self):
        st.title("📈 차트 페이지")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"]
        )
        st.line_chart(chart_data)


# -------------------------
# Form Page
# -------------------------
class InputPage:
    def __init__(self):
        st.title("📝 입력 페이지")
        name = st.text_input("이름을 입력하세요")
        age = st.number_input("나이를 입력하세요", 0, 120)
        if name:
            st.success(f"안녕하세요, {name}님! 나이는 {age}세입니다.")


# -------------------------
# 페이지 등록
# -------------------------
Page_Home  = st.Page(HomePage,  title="Home",  icon="🏠", url_path="home", default=True)
Page_Data  = st.Page(DataPage,  title="Data",  icon="📊", url_path="data")
Page_Chart = st.Page(ChartPage, title="Chart", icon="📈", url_path="chart")
Page_Form  = st.Page(InputPage, title="Form",  icon="📝", url_path="form")

pages = [Page_Home, Page_Data, Page_Chart, Page_Form]

# -------------------------
# 네비게이션 실행
# -------------------------
selected_page = st.navigation(pages)
selected_page.run()
