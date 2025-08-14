import streamlit as st

# 데이터 준비
mbti_jobs = {
    "INTJ": ["연구원", "전략기획자", "데이터 분석가"],
    "ENFP": ["마케터", "작가", "디자이너"],
    "ISTJ": ["회계사", "관리자", "엔지니어"],
    "ESFP": ["배우", "강사", "이벤트 기획자"],
    "ENTP": ["스타트업 창업가", "컨설턴트", "광고 기획자"],
    # ... 나머지 MBTI 추가
}

# 제목
st.title("MBTI 기반 직업 추천 사이트")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 버튼 클릭 시 결과 출력
if st.button("직업 추천 받기"):
    jobs = mbti_jobs.get(selected_mbti, [])
    if jobs:
        st.subheader(f"{selected_mbti} 유형 추천 직업")
        for job in jobs:
            st.write(f"✅ {job}")
    else:
        st.warning("해당 MBTI에 대한 데이터가 없습니다.")

