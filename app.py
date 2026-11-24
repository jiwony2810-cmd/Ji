import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎮")

st.title("🎮 1~100 숫자 맞추기 (Up & Down)")
st.write("컴퓨터가 생각한 1부터 100 사이의 비밀 숫자를 맞춰보세요!")

# 게임 상태 초기화 (세션 유지)
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []

# 숫자 입력 폼
with st.form(key="guess_form", clear_on_submit=True):
    guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)
    submit = st.form_submit_button("정답 확인!")

# 버튼 클릭 시 로직
if submit and not st.session_state.game_over:
    st.session_state.attempts += 1
    target = st.session_state.target

    if guess < target:
        msg = f"🔼 **{guess}** 보다 **UP!** (더 큰 숫자입니다)"
        st.warning(msg)
        st.session_state.history.append(msg)
    elif guess > target:
        msg = f"🔽 **{guess}** 보다 **DOWN!** (더 작은 숫자입니다)"
        st.info(msg)
        st.session_state.history.append(msg)
    else:
        st.balloons()
        st.success(f"🎉 정답입니다! **{st.session_state.attempts}번** 만에 맞추셨습니다!")
        st.session_state.game_over = True

# 이전 입력 기록 표시
if st.session_state.history:
    with st.expander("이전 시도 기록 보기", expanded=True):
        for item in reversed(st.session_state.history):
            st.write(item)

# 새 게임 시작 버튼
if st.session_state.game_over:
    if st.button("🔄 새 게임 시작하기"):
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.history = []
        st.rerun()
