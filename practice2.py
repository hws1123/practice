import streamlit as st
import pyrebase
import time
from datetime import date

# ---------------------
# Firebase 설정
# ---------------------
firebase_config = {
    "apiKey": "AIzaSyCswFmrOGU3FyLYxwbNPTp7hvQxLfTPIZw",
    "authDomain": "sw-projects-49798.firebaseapp.com",
    "databaseURL": "https://sw-projects-49798-default-rtdb.firebaseio.com",
    "projectId": "sw-projects-49798",
    "storageBucket": "sw-projects-49798.appspot.com",
    "messagingSenderId": "812186368395",
    "appId": "1:812186368395:web:be2f7291ce54396209d78e"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
firestore = firebase.database()

# ---------------------
# 세션 상태 초기화
# ---------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.session_state.id_token = ""

# ---------------------
# 로그인 페이지 클래스
# ---------------------
class LoginPage:
    def show(self):
        st.title("🔐 로그인")
        email = st.text_input("이메일", key="login_email")
        password = st.text_input("비밀번호", type="password", key="login_pw")
        if st.button("로그인", key="login_btn"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.id_token = user["idToken"]
                st.success("로그인 성공!")
                time.sleep(1)
                st.rerun()
            except:
                st.error("로그인 실패")

# ---------------------
# 회원가입 페이지 클래스
# ---------------------
class RegisterPage:
    def show(self):
        st.title("📝 회원가입")
        email = st.text_input("이메일", key="register_email")
        password = st.text_input("비밀번호", type="password", key="register_pw")
        if st.button("회원가입", key="register_btn"):
            try:
                auth.create_user_with_email_and_password(email, password)
                firestore.child("users").child(email.replace(".", "_")).set({
                    "email": email
                })
                st.success("회원가입 성공! 로그인 해주세요.")
            except:
                st.error("회원가입 실패")

# ---------------------
# 로그아웃 클래스
# ---------------------
class LogoutPage:
    def show(self):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.session_state.id_token = ""
        st.success("로그아웃 되었습니다.")
        time.sleep(1)
        st.rerun()

# ---------------------
# 일기장 페이지 클래스
# ---------------------
class DiaryPage:
    def show(self):
        st.title("📘 나의 일기장")

        user_id = st.session_state.user_email.replace(".", "_")
        diary_ref = firestore.child("diary").child(user_id)

        st.subheader("✏️ 오늘의 일기 작성")
        entry_date = st.date_input("날짜", value=date.today(), key="diary_date")
        content = st.text_area("내용을 입력하세요", height=200, key="diary_content")

        if st.button("저장", key="save_diary_btn"):
            if not content.strip():
                st.warning("내용을 입력해주세요.")
            else:
                diary_ref.child(str(entry_date)).set({
                    "date": str(entry_date),
                    "content": content
                })
                st.success("✅ 일기 저장 완료!")

        st.divider()
        st.subheader("📖 일기 목록")

        entries = diary_ref.get().val()
        if entries:
            for day, entry in sorted(entries.items(), reverse=True):
                with st.expander(f"📅 {day}"):
                    st.write(entry.get("content", ""))
        else:
            st.info("작성된 일기가 없습니다.")

# ---------------------
# 페이지 실행 로직
# ---------------------
if st.session_state.logged_in:
    menu = st.sidebar.radio("메뉴", ["일기장", "로그아웃"], key="menu_auth")
    if menu == "일기장":
        DiaryPage().show()
    elif menu == "로그아웃":
        LogoutPage().show()
else:
    menu = st.sidebar.radio("메뉴", ["로그인", "회원가입"], key="menu_guest")
    if menu == "로그인":
        LoginPage().show()
    elif menu == "회원가입":
        RegisterPage().show()
