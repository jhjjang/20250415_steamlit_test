import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Hello from test1!")
    st.set_page_config(
    page_title="UV + Streamlit demo",
    page_icon="📊",
    layout="wide"
    )
    st.title("UV와 Streamlit을 활용한 데이터 분석 앱")
    st.markdown("""
    이 앱은 UV로 환경을 관리하고 Streamlit으로 구현된 데이터 시각화 도구입니다.
    간단한 데이터 생성, 분석 및 시각화 기능을 제공합니다.
    """)

    st.sidebar.header("데이터 파라미터 설정")
    num_points = st.sidebar.slider("데이터 포인트 수", 10, 1000, 100)
    noise_level = st.sidebar.slider("노이즈 수준", 0.0, 2.0, 0.5)
    trend_type = st.sidebar.selectbox("트렌드 유형", ["선형", "지수", "사인파"])


if __name__ == "__main__":
    main()
