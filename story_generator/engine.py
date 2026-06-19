from openai import OpenAI
from .config import OPENAI_API_KEY
from . import templates

class BedtimeStoryEngine:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_story(self, child_name: str, child_age: int, prompt_keywords: str, theme: str) -> str:
        """
        Generates a 5-minute tailored bedtime story using OpenAI's chat completion.
        """
        formatted_system = templates.SYSTEM_PROMPT.format(
            child_name=child_name,
            child_age=child_age,
            prompt_keywords=prompt_keywords,
            theme=theme
        )
        
        formatted_user = templates.USER_PROMPT_TEMPLATE.format(
            child_name=child_name,
            child_age=child_age,
            prompt_keywords=prompt_keywords,
            theme=theme
        )

        try:
            # Using gpt-4o-mini: exceptionally fast, smart, and ultra-cheap
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": formatted_system},
                    {"role": "user", "content": formatted_user}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"An error occurred while weaving your story: {str(e)}"