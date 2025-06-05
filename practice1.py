
import streamlit as st
import pandas as pd
import numpy as np

# 📘 탭 1: 소개 페이지
class IntroPage:
    def render(self):
        st.title("🎉 Streamlit 앱에 오신 것을 환영합니다")
        st.markdown("이 앱은 클래스 기반 구조로 구성된 **멀티 탭 웹앱**입니다.")
        st.caption("탭마다 고유한 클래스를 통해 구성됩니다.")


# 📗 탭 2: 데이터 확인
class DataPage:
    def render(self):
        st.title("📊 데이터 미리보기")
        df = pd.DataFrame({
            "이름": ["Alice", "Bob", "Charlie", "David"],
            "점수": [85, 90, 78, 92]
        })
        st.write("데이터프레임을 아래에 보여드립니다:")
        st.dataframe(df)


# 📕 탭 3: 시각화
class ChartPage:
    def render(self):
        st.title("📈 랜덤 차트")
        data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"]
        )
        st.line_chart(data)


# 📙 탭 4: 사용자 입력
class InputPage:
    def render(self):
        st.title("📝 사용자 입력")
        name = st.text_input("이름을 입력하세요:")
        age = st.number_input("나이를 입력하세요:", 0, 120)

        if name:
            st.success(f"안녕하세요, {name}님! 나이는 {age}세로 입력하셨습니다.")


# 각 탭을 이름과 클래스 인스턴스로 매핑
tabs = {
    "소개": IntroPage(),
    "데이터": DataPage(),
    "차트": ChartPage(),
    "입력폼": InputPage()
}

# 탭 UI 생성
selected_tab = st.tabs(list(tabs.keys()))

# 각 탭에 맞는 클래스 렌더링
for i, key in enumerate(tabs.keys()):
    with selected_tab[i]:
        tabs[key].render()