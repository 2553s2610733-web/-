import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="소개팅 앱",
    page_icon="💕",
    layout="centered"
)

# 세션 상태 초기화
if "profiles" not in st.session_state:
    st.session_state.profiles = []

if "likes" not in st.session_state:
    st.session_state.likes = []

# 제목
st.title("💕 소개팅 앱")
st.write("간단한 스트림릿 소개팅 서비스")

menu = st.sidebar.selectbox(
    "메뉴 선택",
    ["프로필 등록", "매칭 보기", "좋아요 목록"]
)

# -------------------------
# 프로필 등록
# -------------------------
if menu == "프로필 등록":

    st.header("내 프로필 등록")

    with st.form("profile_form"):

        name = st.text_input("이름")
        age = st.number_input("나이", 18, 100, 25)
        gender = st.selectbox("성별", ["남성", "여성"])
        hobby = st.text_input("취미")
        intro = st.text_area("자기소개")
        photo = st.file_uploader(
            "프로필 사진",
            type=["png", "jpg", "jpeg"]
        )

        submit = st.form_submit_button("등록하기")

        if submit:

            if name.strip() == "":
                st.error("이름을 입력해주세요.")
            else:

                profile = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "hobby": hobby,
                    "intro": intro,
                    "photo": photo
                }

                st.session_state.profiles.append(profile)

                st.success(f"{name}님의 프로필이 등록되었습니다!")

# -------------------------
# 매칭 보기
# -------------------------
elif menu == "매칭 보기":

    st.header("추천 프로필")

    profiles = st.session_state.profiles

    if len(profiles) == 0:
        st.warning("등록된 프로필이 없습니다.")
    else:

        profile = random.choice(profiles)

        st.subheader(profile["name"])

        if profile["photo"] is not None:
            st.image(profile["photo"], width=250)

        st.write(f"🎂 나이: {profile['age']}")
        st.write(f"⚧ 성별: {profile['gender']}")
        st.write(f"🎯 취미: {profile['hobby']}")
        st.write(f"📝 소개: {profile['intro']}")

        if st.button("❤️ 좋아요"):

            st.session_state.likes.append(profile)

            st.success(f"{profile['name']}님에게 좋아요를 보냈습니다!")

# -------------------------
# 좋아요 목록
# -------------------------
elif menu == "좋아요 목록":

    st.header("내가 좋아요한 사람")

    likes = st.session_state.likes

    if len(likes) == 0:
        st.info("아직 좋아요한 사람이 없습니다.")
    else:

        for idx, person in enumerate(likes):

            st.subheader(f"{idx + 1}. {person['name']}")

            if person["photo"] is not None:
                st.image(person["photo"], width=150)

            st.write(f"나이: {person['age']}")
            st.write(f"취미: {person['hobby']}")
            st.write("---")
