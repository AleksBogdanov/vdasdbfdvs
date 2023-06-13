import streamlit as st
from st_pages import Page, show_pages, add_page_title


def main():
    """Main Page containing all the pages of app"""
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Създайте кратко резюме на документ по Ваш избор </h1>",
        unsafe_allow_html=True)  # Name displayed on the page
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Задайте въпрос към Конституцията на България или към ваш документ</h1>",
        unsafe_allow_html=True)  # Name displayed on the page
    show_pages(
        [
            Page("summary_page.py", "Резюме", "📝"),
            Page("qna_over_your_doc.py", "Q&A ", "❓"),
            Page("qna_bg_constitution.py", "Конституция", "️🏛"),

        ]
    )

if __name__ == "__main__":
    main()