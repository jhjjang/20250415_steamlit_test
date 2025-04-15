import sys
import streamlit as st
st.set_page_config(
    initial_sidebar_state = "collapsed",
    layout = "wide",
    page_icon = "",
    page_title = "Streamlit Love"
)

st.text("안녕하세요!!~~")

my_text = "변수안에 있는 텍스트입니다."
#st.text(my_text)
#st.markdown("This is **text**")
#st.markdown("## This is Title")

#st.title("Title1")
#st.header("Header1")
#st.subheader("Subheader1")


st.write("general text")
st.write("This is markdown **String**")
st.write("## Title")

test1 = 1
test2 = [1,2,3]
test3 = {"name":"jang","age":30}

st.write(test1)
st.write(test2)
st.write(test3)


with st.sidebar:
    st.write("This is sidebar")
    st.write("You can close this tap")



col1, col2, col3 = st.columns([2,5,1])

with col1:
    st.write("left")
    st.write("This is markdown **String1**")
    st.write("Title1")

with col2:
    st.write("center")
    st.write("This is markdown **String2**")
    st.write("Title2")

with col3:
    st.write("right")
    st.write("This is markdown **String3**")
    st.write("Title3")

st.write("--------------------- general text ---------------------")

my_button = st.button("My Button")
st.write(my_button)
if my_button == True:
    st.write("When you click button, see this text")

st.write(sys.version)
#st.link_button("Onchannel","https://www.onch3.co.kr")

st.markdown("[Onchannel](https://www.onch3.co.kr)")


text_input = st.text_input("입력하세요")
if text_input:
    st.write(f"사용자가 입력한 내용은 {text_input}")

option = st.selectbox("Select one",[1,2,3,4])
st.write(option)

uploaded_file = st.file_uploader("파일을 업록드하세요")
if uploaded_file:
    st.write(uploaded_file.name)
    file_content = uploaded_file.read().decode("utf-8")
    st.write(file_content)


data = """이것은 다운로드 데이터입니다.
여러 줄의 예시에서 텍스트를 작성하여 다운로드 기능을 테스트합니다.
이 데이터는 Streamlit에서 다운로드 버튼을 누르면 저장됩니다.
예제 데이터를 다운로드하여 기능을 확인해 보세요.
"""

download_button = st.download_button("Download", data=data, file_name="result.txt")

if "counter" not in st.session_state:
    st.session_state.counter = 0

button = st.button("Click!!")

if button:
    st.session_state.counter = st.session_state.counter + 1

st.write(st.session_state.counter)
