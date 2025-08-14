import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="🌟 MBTI 직업 추천 사이트 🌟", page_icon="💼", layout="centered")

# 🌈 스타일 커스터마이징
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #FF6F61;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px #00000020;
    }
    .subtitle {
        font-size: 22px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .job-card {
        background-color: #FFF3E4;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 🗂 MBTI별 직업 데이터
mbti_jobs = {
    "INTJ": ["🔬 연구원", "📊 전략기획자", "📈 데이터 분석가"],
    "ENTP": ["🚀 스타트업 창업가", "🧠 컨설턴트", "🎯 광고 기획자"],
    "ENFP": ["🎨 마케터", "✍️ 작가", "🖌 디자이너"],
    "ISTJ": ["📒 회계사", "📂 관리자", "⚙️ 엔지니어"],
    "ESFP": ["🎭 배우", "🎤 강사", "🎉 이벤트 기획자"],
    "INFJ": ["🩺 상담가", "📚 작가", "🌱 사회운동가"],
    "INFP": ["🎶 작곡가", "🎨 일러스트레이터", "📖 시인"],
    "ESTP": ["🏆 스포츠 코치", "💼 영업사원", "📢 홍보 담당자"],
    "ISTP": ["🔧 기술자", "🚗 자동차 정비사", "🛠 발명가"],
    "ENTJ": ["🏢 CEO", "📈 경영 전략가", "🧭 프로젝트 매니저"],
    "ENFJ": ["🤝 인사담당자", "🎤 연설가", "🎯 교육 전문가"],
    "ISFJ": ["🏥 간호사", "🛎 서비스 매니저", "📋 행정 담당자"],
    "ESFJ": ["🍽 요리사", "🎈 행사 기획자", "🏨 호텔 매니저"],
    "ISFP": ["📷 사진작가", "🎶 뮤지션", "🎨 화가"],
    "ESTJ": ["📦 물류 관리자", "💵 금융 전문가", "🏭 생산 관리자"],
    "INTP": ["🖥 프로그래머", "🧪 연구원", "🔍 분석가"],
}

# 🌟 타이틀
st.markdown('<div class="title">🌟 MBTI 기반 직업 추천 사이트 💼✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI에 딱 맞는 직업을 추천해드립니다! 🚀</div>', unsafe_allow_html=True)

# 📌 MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("🔍 MBTI를 선택하세요:", mbti_list)

# 🎯 추천 버튼
if st.button("🌟 추천 받기 💡"):
    jobs = mbti_jobs.get(selected_mbti, [])
    st.markdown(f"<h3>💫 {selected_mbti} 유형 추천 직업 💫</h3>", unsafe_allow_html=True)
    for job in jobs:
        st.markdown(f'<div class="job-card">{job}</div>', unsafe_allow_html=True)
    st.balloons()  # 🎈 애니메이션 효과
