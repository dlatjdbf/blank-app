import streamlit as st
if "selected" not in st.session_state:
    st.session_state.selected = None

# 페이지 설정
st.set_page_config(page_title="Dose to Food", layout="centered")

# 커스텀 폰트 적용 (옵션)
st.markdown(
    "<h1 style='font-family: Pacifico, cursive; text-align:center;'>Dose to Food</h1>",
    unsafe_allow_html=True
)
st.write("---")

# 검색창
query = st.text_input("Search for a drug...", "")

# 예시 약물 리스트
drugs = ["Ibuprofen", "Paracetamol", "Aspirin",
         "Naproxen", "Omeprazole", "Cetirizine"]

# 필터링
filtered = [d for d in drugs if query.lower() in d.lower()]

# 3열 그리드로 버튼 배치
cols = st.columns(3)
for idx, drug in enumerate(filtered):
    with cols[idx % 3]:
      

# — 아래부터 상세 뷰 시작 —
# Session State 초기화 (파일 최상단 한 번만 해 주셔도 됩니다)
if "selected" not in st.session_state:
    st.session_state.selected = None


# 선택된 약물이 있으면 상세 카드 렌더링
if st.session_state.selected:
    info = {
        "변비약": {
            "side_effect": "과다 복용 시 설사, 복통이 발생할 수 있습니다.",
            "alternatives": ["Kiwi (100g)", "Xylobiose 5g"]
        }
    }[st.session_state.selected]

    st.markdown(f"## {st.session_state.selected} 상세 정보")

    # 부작용 카드 (핑크)
    st.markdown(f"""
    <div style="
      background:#fde2e4;
      padding:16px;
      border-radius:8px;
      margin-bottom:12px;
    ">
      <strong>약의 부작용</strong><br>
      {info['side_effect']}
    </div>
    """, unsafe_allow_html=True)

    # 대체 성분/음식 카드 (옐로우)
    for idx, alt in enumerate(info["alternatives"], start=1):
        st.markdown(f"""
        <div style="
          background:#fff3bf;
          padding:16px;
          border-radius:8px;
          margin-bottom:12px;
        ">
          <strong>대체 성분/음식 {idx}</strong><br>
          {alt}
        </div>
        """, unsafe_allow_html=True)
# — 상세 뷰 끝 —
# 버튼을 동그랗게 만드는 CSS
st.markdown("""
<style>
div.stButton > button:first-child {
  width: 100px; height: 100px;
  border-radius: 50%;
  background-color: #dce5ff;
  font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
