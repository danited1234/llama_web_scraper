import streamlit as st
from scrape import Scrape
from parsing import parse_with_ollamm

number_of_scrolls = 0


st.title(" 👨‍🔧 Scraping Made Easy")
url = st.text_input("Enter a Website URL: ")
options = st.selectbox("Select Options To Scrape Websites",
                       ("Scrape Multiple Webpage (Seprated By Comma In Input Field)","Scroll Web Page"))
if options:
    if "Scrape Multiple Webpages (Seprated By Comma)" in options:
        url = url.split(",")

    if "Scroll" in options:
        number_of_scrolls = st.slider(label="Select Scrolls",min_value=1,max_value=100)
        


if st.button("Scarpe Site"):
    if url:
        st.write("Scraping the website")
        print(number_of_scrolls)
        result = Scrape().scrape_website(url,int(number_of_scrolls))
        # print(result)
        st.session_state.result = result
        with st.expander("View Website Content"):
            st.text_area("Website Content",result,height=300)

if "result" in st.session_state:
    parse_description = st.text_area("Describe what data you want to extract")
    if st.button("Extract Content"):
        if parse_description:
            st.write("Extracting Content")
            extracted_text = parse_with_ollamm(st.session_state.result,parse_description)
            st.write(extracted_text,unsafe_allow_html=True)