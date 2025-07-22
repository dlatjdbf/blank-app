import streamlit as st

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
        if st.button(drug, key=drug):
            st.write(f"Selected: **{drug}** – natural alternatives coming soon!")

# 버튼을 동그랗게 만드는 CSS
st.markdown("""
st.markdown("""
<style>
  /* 컬럼 컨테이너를 가운데로 */
  [data-testid="stColumns"] { justify-content: center !important; }
  /* 버튼(동그라미) 글씨를 진하게 */
  div.stButton > button { font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)
<style>
div.stButton > button:first-child {
  width: 100px; height: 100px;
  border-radius: 50%;
  background-color: #dce5ff;
  font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
