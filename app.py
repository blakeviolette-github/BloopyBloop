import streamlit as st
from story_generator import BedtimeStoryEngine

# 1. Page Configuration (Sets title and a cloud emoji for StoryPuff)
st.set_page_config(
    page_title="StoryPuff - Custom Bedtime Stories",
    page_icon="☁️",
    layout="centered"
)

# 2. Inject some custom styling to give it a soft, magical bedtime vibe
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f9fc;
    }
    h1 {
        color: #4A3E65;
        text-align: center;
        font-family: 'Cozy', sans-serif;
    }
    .story-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        font-size: 1.15rem;
        line-height: 1.8;
        color: #2D2D2D;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Setup
st.title("☁️ StoryPuff")
st.subheader("Turn tonight's wild thoughts into a cozy bedtime tale.", divider="rainbow")

# Initialize the AI engine
@st.cache_resource
def get_engine():
    return BedtimeStoryEngine()

try:
    engine = get_engine()
except Exception as e:
    st.error(f"Configuration Error: {e}. Make sure your .env file has your OPENAI_API_KEY!")
    st.stop()

# 4. User Input Form
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
        placeholder="e.g., a blue garbage truck traveling through space looking for stars, or a tiny dragon learning to share his crayons..."
    )

    st.markdown("### 📚 Story Vibe")
    theme = st.selectbox(
        "Choose the tone for tonight:",
        ["Calming & Sleepy", "Educational (Sneak in real facts!)", "Whimsical & Silly", "A Story with a Moral Lesson"]
    )

    # Submit button
    generate_btn = st.button("✨ Weave My Bedtime Story", use_container_width=True)

# 5. Generation & Display Logic
if generate_btn:
    # Validation
    if not child_name:
        child_name = "Little Adventurer"
    if not prompt_keywords:
        st.warning("Please enter a few words or a topic your child is thinking about!")
        st.stop()

    # Animated loading text while calling OpenAI
    with st.spinner("✨ Creating your custom StoryPuff tale... Fluffing up the blankets..."):
        story_text = engine.generate_story(
            child_name=child_name,
            child_age=child_age,
            prompt_keywords=prompt_keywords,
            theme=theme
        )
    
    # Present the story inside a beautiful, readable layout
    st.success("🛌 Ready to read!")
    
    st.markdown("### 📖 Tonight's Masterpiece")
    # Wrap story text in a styled container block
    st.markdown(f"<div class='story-box'>{story_text}</div>", unsafe_allow_html=True)
    
    st.balloons()  # Fun celebration drop for the child to see!