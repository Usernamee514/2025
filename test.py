# app.py
# -*- coding: utf-8 -*-
import streamlit as st
import random

# -----------------------------
# 감정별 영화 추천 데이터
# -----------------------------
movies_by_emotion = {
    "행복 😊": [
        {"title": "극한직업", "year": 2019, "desc": "통쾌하고 유쾌한 수사 코미디"},
        {"title": "인턴", "year": 2015, "desc": "따뜻하고 유쾌한 직장 힐링 드라마"}
    ],
    "슬픔 😢": [
        {"title": "이터널 선샤인", "year": 2004, "desc": "사랑과 기억에 대한 독특한 이야기"},
        {"title": "인사이드 아웃", "year": 2015, "desc": "마음을 어루만지는 감정 모험"}
    ],
    "화남 😡": [
        {"title": "존 윅", "year": 2014, "desc": "짜증날 때 시원한 액션"},
        {"title": "범죄도시", "year": 2017, "desc": "사이다 액션으로 스트레스 해소"}
    ],
    "설렘 💘": [
        {"title": "어바웃 타임", "year": 2013, "desc": "시간여행을 통해 찾아가는 사랑"},
        {"title": "너의 이름은.", "year": 2016, "desc": "운명 같은 인연의 만남"}
    ],
    "우울 🌧️": [
        {"title": "소울", "year": 2020, "desc": "삶의 의미를 되찾는 따뜻한 여정"},
        {"title": "리틀 포레스트", "year": 2018, "desc": "자연 속에서 쉬어가는 힐링 드라마"}
    ],
    "기분전환 🎉": [
        {"title": "주토피아", "year": 2016, "desc": "귀엽고 유쾌한 모험"},
        {"title": "가디언즈 오브 갤럭시", "year": 2014, "desc": "레트로 음악과 함께하는 우주 액션"}
    ],
}

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="🎬 기분 따라 영화 추천", page_icon="🎥", layout="centered")

st.title("🎬 기분 따라 영화 추천")
st.write("오늘의 기분을 선택하면, 어울리는 영화를 추천해드릴게요!")

# -----------------------------
# 감정 선택
# -----------------------------
emotion = st.radio(
    "현재 기분을 골라주세요:",
    list(movies_by_emotion.keys()),
    horizontal=True
)

# -----------------------------
# 팝콘 폭죽 애니메이션 (랜덤 위치 여러 개 생성)
# -----------------------------
def popcorn_explosion(n=25):
    css = """
    <style>
    @keyframes explode {
      0%   { transform: translateY(0) scale(0.8); opacity: 1; }
      70%  { transform: translateY(-200px) scale(1.2) rotate(20deg); opacity: 1; }
      100% { transform: translateY(-300px) scale(0.6) rotate(-20deg); opacity: 0; }
    }
    .pop {
      position: fixed;
      bottom: 0;
      font-size: 2rem;
      animation: explode 2s ease-out forwards;
      z-index: 9999;
    }
    </style>
    """
    divs = []
    for i in range(n):
        left = random.randint(0, 90)   # 화면 가로 위치 %
        delay = round(random.uniform(0, 1.5), 2)  # 폭죽이 터지는 시점 랜덤
        size = random.choice(["1.5rem","2rem","2.5rem"])
        divs.append(
            f'<div class="pop" style="left:{left}%; animation-delay:{delay}s; font-size:{size};">🍿</div>'
        )
    return css + "\n".join(divs)

# -----------------------------
# 추천 결과 표시
# -----------------------------
if emotion:
    st.subheader(f"✨ {emotion} 기분일 때 추천 영화")
    movies = movies_by_emotion[emotion]
    for m in movies:
        st.markdown(f"**🎞️ {m['title']} ({m['year']})**")
        st.write(f"👉 {m['desc']}")
        st.markdown("---")

    # 팝콘 폭죽 효과 출력
    st.markdown(popcorn_explosion(30), unsafe_allow_html=True)

