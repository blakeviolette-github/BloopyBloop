from setuptools import setup, find_packages

setup(
    name="story_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
)