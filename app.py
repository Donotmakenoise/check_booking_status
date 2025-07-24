import streamlit as st
import pandas as pd
import requests
import html
import unicodedata
import re
import time
from io import BytesIO

# Normalize HTML
def normalize_text(text):
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()

# Check Booking URL
def check_booking_status(url):
    url = url.split("?")[0]
    if pd.isna(url) or not isinstance(url, str) or not url.startswith("http"):
        return "❌ Invalid or Empty URL"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, allow_redirects=True, headers=headers, timeout=10)
        final_url = response.url.split("?")[0]

        if response.history:
            if "searchresults" in final_url:
                return "🔁 Redirected to Listing Page"
            elif "/hotel/" in final_url and final_url != url:
                return "➡️ Redirected Hotel page to current URL format"
            else:
                return "🔁 Redirected to Listing Page"

        if response.status_code == 200:
            html_text = normalize_text(response.text)
            unavailable_phrases = [
                "not taking reservations",
                "temporarily unavailable on our site",
                "no rooms available at this property",
                "isnt bookable on our site",
                "currently not possible to make",
                "not possible to make reservations",
                "not possible to make reservations for this hotel"
            ]
            for phrase in unavailable_phrases:
                if phrase in html_text:
                    return "❌ Not Taking Reservations"
            return "✅ Available"
        else:
            return f"⚠️ HTTP {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {str(e)}"
    finally:
        time.sleep(1)

# --- Streamlit Interface ---
st.title("🔍 Booking URL Status Checker")
st.markdown("Upload an Excel file with a `URL` column to check booking availability.")

uploaded_file = st.file_uploader("Choose Excel file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    if "URL" not in df.columns:
        st.error("❌ Excel file must contain a 'URL' column.")
    else:
        with st.spinner("Checking URLs..."):
            df["Status"] = df["URL"].apply(check_booking_status)

        st.success("✅ Done!")

        # Show result
        st.dataframe(df)

        # Download link
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        st.download_button("📥 Download Result Excel", output, "booking_status_results.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
