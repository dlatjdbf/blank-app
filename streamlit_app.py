import streamlit as st
# ─── 세션 상태 초기화 ───────────────────────────────────────────
if "selected" not in st.session_state:
    st.session_state.selected = None

# ─── 페이지 설정 ─────────────────────────────────────────────────
st.set_page_config(page_title="Dose to Food", layout="centered")

# ─── 타이틀 ─────────────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center; font-family:Pacifico, cursive;'>Dose to Food</h1>",
    unsafe_allow_html=True,
)
st.write("---")

# ─── 검색창 ─────────────────────────────────────────────────────
query = st.text_input("약물 검색...", "")

# ─── 약물 리스트 & 필터링 ───────────────────────────────────────
drugs = ["변비약"]  # 예시: 변비약
filtered = [d for d in drugs if query.lower() in d.lower()]

# ─── 버튼 그리드 (3열) ─────────────────────────────────────────
cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
        # 토글 로직: 같은 약을 다시 누르면 해제
        if st.button(drug, key=f"btn_{drug}"):
            if st.session_state.selected == drug:
                st.session_state.selected = None
            else:
                st.session_state.selected = drug

# ─── 상세 뷰 (선택된 약물이 있으면) ─────────────────────────────
if st.session_state.selected:
    # 데이터 매핑
    info_map = {
        "변비약": {
            "side_effect": "과다 복용 시 설사, 복통이 발생할 수 있습니다.",
            "alternatives": ["Kiwi (100g)", "Xylobiose 5g"],
        }
    }
    info = info_map[st.session_state.selected]

    # 제목을 검정색으로
    st.markdown(
        f"<h2 style='color:#000; text-align:left;'>{st.session_state.selected} 상세 정보</h2>",
        unsafe_allow_html=True,
    )

    # 부작용 카드 (핑크), 텍스트도 검정
    st.markdown(
        f"""
        <div style="
            background:#fde2e4;
            color:#000;
            padding:16px;
            border-radius:8px;
            margin-bottom:12px;
        ">
            <strong>약의 부작용</strong><br>
            {info['side_effect']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 대체 성분/음식 카드 (옐로우), 텍스트 검정
    for i, alt in enumerate(info["alternatives"], start=1):
        st.markdown(
            f"""
            <div style="
                background:#fff3bf;
                color:#000;
                padding:16px;
                border-radius:8px;
                margin-bottom:12px;
            ">
                <strong>대체 성분/음식 {i}</strong><br>
                {alt}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─── 전역 CSS ───────────────────────────────────────────────────
st.markdown(
    """
    <style>
      /* 버튼 그리드 컨테이너 가운데 정렬 */
      [data-testid="stColumns"] { justify-content: center !important; }
      /* 원형 버튼, 글씨 볼드 & 검정 고정 */
      div.stButton > button:first-child {
        width: 100px; height: 100px;
        border-radius: 50%;
        background-color: #dce5ff;
        font-weight: bold;
        color: #000 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)
