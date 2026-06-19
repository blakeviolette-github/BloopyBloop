import sys
from story_generator import BedtimeStoryEngine

def main():
    try:
        # Initialize the StoryPuff engine
        engine = BedtimeStoryEngine()
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        sys.exit(1)

    print("\n" + "="*45)
    print("✨ WELCOME TO STORYPUFF: THE BEDTIME ENGINE ✨")
    print("="*45)
    print("Let's capture tonight's sparks before drifting off to sleep.\n")

    # 1. Gather child's details
    child_name = input("👤 What is the child's name? ").strip()
    if not child_name:
        child_name = "Little Adventurer"

    while True:
        try:
            age_input = input(f"🎂 How old is {child_name}? ")
            child_age = int(age_input)
            break
        except ValueError:
            print("Please enter a valid number for the age!")

    # 2. Capture the core feature: Child's random ideas
    print(f"\n🌙 Ask {child_name}: 'What are we dreaming about tonight?'")
    print("(Example: 'sharks flying in space', 'learning how bees make honey', 'sharing toys')")
    prompt_keywords = input("👉 ")
    
    if not prompt_keywords:
        print("No ideas given? No problem, we'll make up a surprise!")
        prompt_keywords = "a cozy magical forest adventure"

    # 3. Choose the bedtime vibe
    print("\n📚 What kind of vibe do we want tonight?")
    print("1. Calming (Strictly sleep-focused)")
    print("2. Educational (Learn cool real facts)")
    print("3. Whimsical (Pure silly fun)")
    print("4. Moral Lesson (Kindness, sharing, bravery)")
    
    choice = input("Select a number (1-4): ").strip()
    theme_map = {
        "1": "Calming & Sleepy",
        "2": "Educational",
        "3": "Whimsical & Fun",
        "4": "Moral/Emotional Lesson"
    }
    theme = theme_map.get(choice, "Calming & Sleepy")

    # 4. Fire up the engine!
    print(f"\n✨ Weaving a custom 5-minute story for {child_name} about '{prompt_keywords}'...")
    print("Please wait while the blankets get cozy... 😴\n")

    story = engine.generate_story(
        child_name=child_name,
        child_age=child_age,
        prompt_keywords=prompt_keywords,
        theme=theme
    )
    
    print("-"*50)
    print(story)
    print("-"*50)
    print("\n✨ Sweet dreams from StoryPuff! ✨\n")

if __name__ == "__main__":
    main()