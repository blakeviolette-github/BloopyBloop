import os
import streamlit as st
from dotenv import load_dotenv

# 1. Attempt to load local environment variables first
load_dotenv()

# 2. Hybrid check: Fall back to Streamlit Cloud secrets if local os.getenv comes up empty
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY configuration.")