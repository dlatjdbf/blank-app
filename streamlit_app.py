import streamlit as st

# ─── 세션 상태 초기화 ───────────────────────────────────────────
if "selected" not in st.session_state:
    st.session_state.selected = None

# ─── 페이지 설정 ─────────────────────────────────────────────────
st.set_page_config(page_title="Dose to Food", layout="centered")

# ─── 타이틀 ───────────────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center; font-family:Pacifico, cursive;'>Dose to Food</h1>",
    unsafe_allow_html=True
)
st.write("---")

# ─── 검색창 ───────────────────────────────────────────────────────
query = st.text_input("약물 검색...", "")

# ─── 약물 리스트 및 필터링 ───────────────────────────────────────
drugs = ["변비약", "수면제"]
filtered = [d for d in drugs if query.lower() in d.lower()]

# ─── 버튼 그리드 (토글 기능 포함) ────────────────────────────────
cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
        clicked = st.button(drug, key=f"btn_{drug}")
        if clicked:
            st.session_state.selected = None if st.session_state.selected == drug else drug

# ─── 상세 뷰 ────────────────────────────────────────────────────
if st.session_state.selected:
    info_map = {
        "변비약": {
            "side_effect": "과다 복용 시 설사, 복통 발생 가능",
            "alternatives": ["키위", "자일로바이오스"],
        },
        "수면제": {
            "side_effect": "과다 복용 시 어지러움, 기억력 저하 발생 가능",
            "alternatives": ["샐러리 & 상추", "우유", "키위", "등푸른생선"],
        },
    }
    sel = st.session_state.selected
    info = info_map[sel]

    # 부작용 카드
    st.markdown(f"""
<div style="
    background:#fde2e4;
    color:#000;
    padding:16px;
    border-radius:8px;
    margin-bottom:12px;
">
    <strong>약의 부작용</strong><br>{info['side_effect']}
</div>
""", unsafe_allow_html=True)

    # 대체 성분/음식 카드 (이제 이름만 한국어)
    for alt in info["alternatives"]:
        st.markdown(f"""
<div style="
    background:#fff3bf;
    color:#000;
    padding:16px;
    border-radius:8px;
    margin-bottom:12px;
">
    <strong>{alt}</strong><br>
    <!-- 상세 설명은 추후 추가 -->
</div>
""", unsafe_allow_html=True)

# ─── CSS 스타일 (원형 버튼 배경 흰색, 텍스트 검정) ─────────────
st.markdown(
    """
    <style>
      /* 버튼 원형, 배경 흰색, 텍스트 검정 */
      div.stButton > button {
          width:100px; height:100px;
          border-radius:50%;
          background-color:#fff !important;
          color:#000 !important;
          font-weight:bold;
          border:1px solid #ccc !important;
      }
      /* 버튼 그리드 중앙 정렬 */
      [data-testid="stColumns"] {
          justify-content:center !important;
      }
      /* 카드 내부 텍스트 검정 */
      div[style*="background:#fde2e4"] *,
      div[style*="background:#fff3bf"] * {
          color:#000 !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)
