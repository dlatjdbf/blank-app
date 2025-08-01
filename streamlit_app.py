import streamlit as st
# — 세션 초기화 (맨 위 한 번만) —
if "sel" not in st.session_state:
    st.session_state.sel = None

st.set_page_config(page_title="Dose to Food", layout="centered")

st.markdown("<h1 style='text-align:center; font-family:Pacifico;'>Dose to Food</h1>", unsafe_allow_html=True)
st.write("---")

query = st.text_input("약물 검색...", "")
drugs = ["변비약"]
filtered = [d for d in drugs if query.lower() in d.lower()]

cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
        # 버튼 클릭 시 토글
        clicked = st.button(drug, key=f"btn_{drug}")
        if clicked:
            if st.session_state.sel == drug:
                st.session_state.sel = None
            else:
                st.session_state.sel = drug

# 상세 뷰
if st.session_state.sel:
    info = {
      "변비약": {
         "side_effect": "과다 복용 시 설사, 복통 발생 가능",
         "alternatives": ["Kiwi (100g)", "Xylobiose 5g"]
      }
    }[st.session_state.sel]

    st.markdown(f"<h2 style='color:#000'>{st.session_state.sel} 상세 정보</h2>", unsafe_allow_html=True)

    # 부작용 카드
    st.markdown(f"""
    <div style="
      background:#fde2e4; color:#000; padding:16px; border-radius:8px; margin-bottom:12px;
    ">
      <strong>약의 부작용</strong><br>{info['side_effect']}
    </div>
    """, unsafe_allow_html=True)

    # 대체 식품 카드
    for i, alt in enumerate(info["alternatives"], 1):
        st.markdown(f"""
        <div style="
          background:#fff3bf; color:#000; padding:16px; border-radius:8px; margin-bottom:12px;
        ">
          <strong>대체 성분/음식 {i}</strong><br>{alt}
        </div>
        """, unsafe_allow_html=True)

# 전역 CSS
st.markdown("""
<style>
  /* 버튼 글자 검정 */
  div.stButton > button { color: #000 !important; }
  /* 카드 내부 텍스트 검정 (백그라운드 기반 선택자) */
  div[style*="background:#fde2e4"] *, div[style*="background:#fff3bf"] * { color: #000 !important; }
  /* 버튼 그리드 중앙 정렬 */
  [data-testid="stColumns"] { justify-content: center !important; }
  /* 버튼 원형, 볼드체 */
  div.stButton > button { width:100px; height:100px; border-radius:50%; font-weight:bold; }
</style>
""", unsafe_allow_html=True)
