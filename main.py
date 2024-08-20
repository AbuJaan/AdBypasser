import random
import streamlit as st
from PyBypass.main import BypasserNotFoundError, UnableToBypassError, UrlConnectionError
import PyBypass as bypasser

st.set_page_config(
    page_title="URL Bypasser",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://discord.gg/mKZGkEK39m",
        "Report a bug": "https://discord.gg/mKZGkEK39m",
        "About": "This is URL Bypasser for ADLINKFLY based website. Made by [BilloXD](https://github.com/AbuJaan)",
    },
)


def random_celeb():
    return random.choice([st.balloons()])


st.title("URL Bypasser")
tab1, tab2, tab3 = st.tabs(
    [
        "Bypass",
        "Batch Bypass",
        "Available Websites",
    ]
)

banned_websites = [
    "linkvertise"
]

__avl_website__ = [
    # List of available websites
]

with tab1:
    show_alert = False
    url = st.text_input(label="Paste your URL")
    if st.button("Submit"):
        if url:
            if any(banned in url for banned in banned_websites):
                st.error("This website is not supported")
                st.stop()
            try:
                with st.spinner("Loading..."):
                    bypassed_link = bypasser.bypass(url)
                    st.success(bypassed_link)

                random_celeb()

                with st.expander("Copy"):
                    st.code(bypassed_link)

            except (
                UnableToBypassError,
                BypasserNotFoundError,
                UrlConnectionError,
            ) as e:
                if show_alert := True:
                    st.error(e)

            if st.button("Dismiss"):
                show_alert = False

        elif show_alert := True:
            st.error("No URLs found")

with tab2:
    st.subheader("Batch Bypass")
    urls = st.text_area(label="Paste your URLs (one per line)").strip().splitlines()
    if st.button("Submit Batch"):
        if urls:
            bypassed_links = []
            errors = []
            for url in urls:
                if any(banned in url for banned in banned_websites):
                    errors.append(f"{url}: This website is not supported")
                else:
                    try:
                        with st.spinner(f"Bypassing {url}..."):
                            bypassed_link = bypasser.bypass(url)
                            bypassed_links.append(bypassed_link)
                    except (UnableToBypassError, BypasserNotFoundError, UrlConnectionError) as e:
                        errors.append(f"{url}: {e}")

            if bypassed_links:
                st.success("Bypassed URLs:")
                for link in bypassed_links:
                    st.write(link)
                random_celeb()

            if errors:
                st.error("Errors encountered:")
                for error in errors:
                    st.write(error)

        else:
            st.error("No URLs provided.")

with tab3:
    st.subheader("Available Websites")
    st.table(__avl_website__)

