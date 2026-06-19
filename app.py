import streamlit as st
import sys
import os

# Ensure the parent directory is in the path so we can find the package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from story_generator.engine import BedtimeStoryEngine

# 1. Page Configuration
st.set_page_config(page_title="BloopyBloop Bedtime Stories", page_icon="☁️", layout="centered")

# 2. Premium Custom Styling
st.markdown("""
    <style>
    .stApp { background-color: #f7f9fc; }
    h1 { color: #3A2E5B; text-align: center; }
    .story-card { background-color: white; padding: 35px; border-radius: 20px; box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.04); font-size: 1.2rem; line-height: 1.9; color: #333333; }
    </style>
""", unsafe_allow_html=True)

st.title("☁️ BloopyBloop")
st.subheader("Turn tonight's wild thoughts into a cozy bedtime tale.", divider="violet")

# Initialize Engine with better debugging
@st.cache_resource
def get_engine():
    try:
        return BedtimeStoryEngine()
    except Exception as e:
        st.error(f"Engine Init Error: {e}")
        return None

engine = get_engine()

# 4. Main User Input Form
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        child_name = st.text_input("Child's Name", value="Little Adventurer")
    with col2:
        child_age = st.number_input("Age", min_value=1, max_value=12, value=5)

    prompt_keywords = st.text_area("What are we dreaming about tonight?", placeholder="e.g., a blue garbage truck in space...")
    theme = st.selectbox("Choose the tone:", ["Calming & Sleepy", "Educational", "Whimsical & Silly", "A Story with a Moral Lesson"])

    generate_btn = st.button("✨ Weave My Bedtime Story", use_container_width=True)

# 5. Story Generation Logic
if generate_btn:
    if not engine:
        st.error("BloopyBloop is currently asleep! The engine failed to start.")
        st.stop()
        
    if not prompt_keywords:
        st.warning("Please tell me what to dream about!")
        st.stop()

    with st.spinner("✨ BloopyBloop is fluffing up the blankets..."):
        try:
            # Diagnostic check: Is the method actually there?
            if not hasattr(engine, 'generate_story'):
                st.error(f"DEBUG: Engine has these methods: {dir(engine)}")
                st.stop()
                
            story_text = engine.generate_story(
                child_name=child_name,
                child_age=child_age,
                prompt_keywords=prompt_keywords,
                theme=theme
            )
            
            st.success("🎉 Your Book is Ready!")
            st.markdown("### 📖 Tonight's Masterpiece")
            st.markdown(f"<div class='story-card'>{story_text}</div>", unsafe_allow_html=True)
            st.balloons()
            
        except Exception as e:
            st.error(f"Error during story generation: {e}")
            import traceback
            st.code(traceback.format_exc())

# 6. Footer
st.divider()
st.caption("What should BloopyBloop learn to do next?")