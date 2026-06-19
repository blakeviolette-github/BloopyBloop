import streamlit as st
from story_generator import BedtimeStoryEngine

# 1. Page Configuration & Title setup
st.set_page_config(
    page_title="BloopyBloop Bedtime Stories",
    page_icon="☁️",
    layout="centered"
)

# 2. Premium Custom Styling (Soft bedtime aesthetic)
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f9fc;
    }
    h1 {
        color: #3A2E5B;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: 800;
    }
    .story-card {
        background-color: white;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.04);
        font-size: 1.2rem;
        line-height: 1.9;
        color: #333333;
    }
    .badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Layout
st.title("☁️ BloopyBloop")
st.subheader("Turn tonight's wild thoughts into a cozy bedtime tale.", divider="violet")

# Initialize the AI Engine cleanly
@st.cache_resource
def get_engine():
    return BedtimeStoryEngine()

try:
    engine = get_engine()
except Exception as e:
    st.error(f"Configuration Error: {e}. Make sure your .env file has your OPENAI_API_KEY!")
    st.stop()

# 4. Main User Input Form
with st.container(border=True):
    st.markdown("### 👤 About the Listener")
    col1, col2 = st.columns(2)
    with col1:
        child_name = st.text_input("Child's Name", placeholder="Leo, Maya, etc.")
    with col2:
        child_age = st.number_input("Age", min_value=1, max_value=12, value=5)

    st.markdown("### 🌙 Tonight's Spark")
    prompt_keywords = st.text_area(
        "What are we dreaming about tonight?",
        placeholder="e.g., a blue garbage truck traveling through space looking for stars, or a tiny dragon learning to share crayons..."
    )

    st.markdown("### 📚 Story Vibe")
    theme = st.selectbox(
        "Choose the tone for tonight:",
        ["Calming & Sleepy", "Educational (Sneak in real facts!)", "Whimsical & Silly", "A Story with a Moral Lesson"]
    )

    # Submit button
    generate_btn = st.button("✨ Weave My Bedtime Story", use_container_width=True)

# 5. Story Generation Logic
if generate_btn:
    if not child_name:
        child_name = "Little Adventurer"
    if not prompt_keywords:
        st.warning("Please enter a few words or a topic your child is thinking about!")
        st.stop()

    # Animated loading spinner while calling the text API
    with st.spinner("✨ BloopyBloop is fluffing up the blankets and weaving your story..."):
        story_text = engine.generate_story(
            child_name=child_name,
            child_age=child_age,
            prompt_keywords=prompt_keywords,
            theme=theme
        )
    
    st.success("🎉 Your Book is Ready!")
    
    # Present the finished story inside a premium, styled layout block
    st.markdown("### 📖 Tonight's Masterpiece")
    st.markdown(f"<div class='story-card'>{story_text}</div>", unsafe_allow_html=True)
    
    st.balloons()  # Fun drop for the kids to watch!

# 6. Interactive Feature-Feedback Section
st.divider()
st.markdown("### 🛠️ Help BloopyBloop Grow!")
st.caption("What should BloopyBloop learn to do next? Test with your family and cast your vote:")

# Create layout buttons for gathering feature feedback
col_vote1, col_vote2, col_vote3 = st.columns(3)
with col_vote1:
    if st.button("🎨 Draw Cover Art", use_container_width=True):
        st.toast("Vote Recorded! You want cover art illustrations.", icon="🎨")
with col_vote2:
    if st.button("🔊 Read Out Loud", use_container_width=True):
        st.toast("Vote Recorded! You want an audio narrator audiobook.", icon="🔊")
with col_vote3:
    if st.button("📚 Child Library", use_container_width=True):
        st.toast("Vote Recorded! You want custom saved bookshelves.", icon="📚")