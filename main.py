import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 學生加分系統")

# 初始化狀態
if "students" not in st.session_state:
    st.session_state.students = {}

# === 初始化學生 ===
st.header("1️⃣ 初始化學生")

student_count = st.number_input(
    "輸入學生人數",
    min_value=1,
    step=1
)

if st.button("建立學生名單"):
    st.session_state.students = {
        i: 0 for i in range(1, student_count + 1)
    }
    st.success("學生名單已建立")

# === 顯示學生狀態（數字版） ===
st.header("2️⃣ 學生分數狀態")

if st.session_state.students:
    cols = st.columns(6)
    for idx, (student_id, score) in enumerate(st.session_state.students.items()):
        with cols[idx % 6]:
            st.image("assets/student.png", width=80)
            st.markdown(f"**{student_id} 號**")
            st.markdown(f"### +{score}")
else:
    st.info("尚未建立學生名單")

# === Enter 即加分 ===
st.header("3️⃣ 快速加分（輸入後按 Enter）")

def add_point_by_enter():
    value = st.session_state.input_id.strip()
    if not value.isdigit():
        return

    student_id = int(value)
    if student_id in st.session_state.students:
        st.session_state.students[student_id] += 1
        st.toast(f"{student_id} 號 +1", icon="➕")

    st.session_state.input_id = ""

st.text_input(
    "輸入學號後直接按 Enter",
    key="input_id",
    on_change=add_point_by_enter
)
