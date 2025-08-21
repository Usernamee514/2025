import streamlit as st
import random

# 전역 변수
emoji_map = {
    "수산물": "❄️",
    "육류": "🥩",
    "유제품": "🥛",
    "곡류": "🌾",
    "과일": "🍎",
    "채소": "🥬"
}

storage_tips = {
    "수산물": ["❄️ 냉장 보관 (0~5℃) 권장, 바로 먹지 않을 경우 냉동 보관.", "👉 밀폐용기 또는 진공 포장하면 신선도 유지!"],
    "육류": ["🥩 냉장 보관은 0~4℃, 장기 보관 시 -18℃ 이하 냉동.", "👉 포장 그대로 두거나 랩으로 감싸 공기 접촉 최소화!"],
    "유제품": ["🥛 0~5℃ 냉장 보관.", "👉 개봉 후 빨리 섭취, 치즈는 밀폐용기에 보관!"],
    "곡류": ["🌾 서늘하고 건조한 곳에 보관.", "👉 장기 보관 시 벌레 방지를 위해 밀폐용기 + 냉장/냉동!"],
    "과일": ["🍎 일부 과일은 실온(바나나, 감), 일부는 냉장(사과, 배) 보관.", "👉 냉장 시 신문지나 랩으로 싸서 수분 증발 방지!"],
    "채소": ["🥬 대부분 냉장 보관, 뿌리채소는 서늘한 실온 보관 가능.", "👉 물기 제거 후 지퍼백이나 밀폐용기에!"]
}

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "select"
if "choice" not in st.session_state:
    st.session_state.choice = None

# 선택 화면
if st.session_state.page == "select":
    st.title("🍱 음식 보관 방법 추천")
    choice = st.selectbox("카테고리를 선택하세요", list(emoji_map.keys()))
    if st.button("보관방법 보기"):
        st.session_state.choice = choice
        st.session_state.page = "result"  # 화면 전환
        # rerun 없이 바로 분기

# 결과 화면
if st.session_state.page == "result":
    choice = st.session_state.choice
    emoji = emoji_map[choice]

    # 5개 이모지 순서대로 떨어지는 애니메이션
    styles = ""
    emoji_divs = ""
    for i in range(5):
        delay = round(i * 0.3, 2)
        start_y = random.randint(150, 250)
        duration = round(random.uniform(0.7, 1.2), 2)
        styles += f"""
        .emoji:nth-child({i+1}) {{
            opacity: 0;
            animation: drop-{i} {duration}s ease forwards;
            animation-delay: {delay}s;
        }}
        @keyframes drop-{i} {{
            0%   {{ transform: translateY(-{start_y}px); opacity: 0; }}
            100% {{ transform: translateY(0); opacity: 1; }}
        }}
        """
        emoji_divs += f"<div class='emoji'>{emoji}</div>"

    st.markdown(
        f"""
        <style>
        .emoji-container {{
            display: flex;
            justify-content: center;
            gap: 20px;
            font-size: 70px;
            margin-bottom: 20px;
        }}
        {styles}
        </style>
        <div class="emoji-container">
            {emoji_divs}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 보관방법 텍스트
    for tip in storage_tips[choice]:
        st.info(tip)

    # 다시 선택 화면으로 돌아가기 버튼
    if st.button("다시 선택"):
        st.session_state.page = "select"
        st.experimental_rerun()
