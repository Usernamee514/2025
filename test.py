import streamlit as st

st.set_page_config(page_title="음식 보관법 추천", page_icon="🍱")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "select"
if "choice" not in st.session_state:
    st.session_state.choice = None

# 보관 방법 딕셔너리 (줄바꿈 포함)
storage_tips = {
    "수산물": "❄️ 냉장 보관 (0~5℃) 권장, 바로 먹지 않을 경우 냉동 보관.\n👉 밀폐용기 또는 진공 포장하면 신선도 유지!",
    "육류": "🥩 냉장 보관은 0~4℃, 장기 보관 시 -18℃ 이하 냉동.\n👉 포장 그대로 두거나 랩으로 감싸 공기 접촉 최소화!",
    "유제품": "🥛 0~5℃ 냉장 보관.\n👉 개봉 후 빨리 섭취, 치즈는 밀폐용기에 보관!",
    "곡류": "🌾 서늘하고 건조한 곳에 보관.\n👉 장기 보관 시 벌레 방지를 위해 밀폐용기 + 냉장/냉동!",
    "과일": "🍎 일부 과일은 실온(바나나, 감), 일부는 냉장(사과, 배) 보관.\n👉 냉장 시 신문지나 랩으로 싸서 수분 증발 방지!",
    "채소": "🥬 대부분 냉장 보관, 뿌리채소는 서늘한 실온 보관 가능.\n👉 물기 제거 후 지퍼백이나 밀폐용기에!"
}

# 페이지: 카테고리 선택
if st.session_state.page == "select":
    st.title("🍱 음식 보관 방법 추천")
    st.write("아래에서 카테고리를 선택하세요!")

    categories = list(storage_tips.keys())
    choice = st.selectbox("카테고리 선택", categories)

    if st.button("확인"):
        st.session_state.choice = choice
        st.session_state.page = "result"
        st.rerun()

# 페이지: 결과 출력
elif st.session_state.page == "result":
    choice = st.session_state.choice
    st.title(f"📦 {choice} 보관 방법")

    # st.markdown을 이용해서 줄바꿈 보장
    st.markdown(
        f"""
        <div style="background-color:#f0f2f6; padding:15px; border-radius:10px;">
        {storage_tips[choice].replace("\n", "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("⬅️ 다시 선택하기"):
        st.session_state.page = "select"
        st.rerun()


# 카테고리별 이모지 매핑
emoji_map = {
    "수산물": "❄️",
    "육류": "🥩",
    "유제품": "🥛",
    "곡류": "🌾",
    "과일": "🍎",
    "채소": "🥬"
}

# 선택된 카테고리에 맞는 이모지
emoji = emoji_map[choice]

# CSS 애니메이션 (이모지 5개 순서대로 떨어지게)
st.markdown(
    f"""
    <style>
    @keyframes drop {{
        0%   {{ transform: translateY(-200px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    .emoji-container {{
        display: flex;
        justify-content: center;
        gap: 20px;
        font-size: 70px;
        margin-bottom: 20px; /* 텍스트와 간격 */
    }}
    .emoji {{
        animation: drop 0.8s ease forwards;
    }}
    .emoji:nth-child(1) {{ animation-delay: 0s; }}
    .emoji:nth-child(2) {{ animation-delay: 0.3s; }}
    .emoji:nth-child(3) {{ animation-delay: 0.6s; }}
    .emoji:nth-child(4) {{ animation-delay: 0.9s; }}
    .emoji:nth-child(5) {{ animation-delay: 1.2s; }}
    </style>
    <div class="emoji-container">
        {''.join([f"<div class='emoji'>{emoji}</div>" for _ in range(5)])}
    </div>
    """,
    unsafe_allow_html=True
)

