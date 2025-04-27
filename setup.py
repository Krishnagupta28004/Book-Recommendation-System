from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System"
AUTHOR_USER_NAME = "Krishna Gupta"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit','numpy', 'pandas', 'matplotlib', 'seaborn']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Krishnagupta28004/Book-Recommendation-System.git",
    packages=[SRC_REPO],
    python_requires=">=3.13",
    install_requires=LIST_OF_REQUIREMENTS
)