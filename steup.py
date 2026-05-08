from setuptools import setup, find_packages
setup(
    name='MCQS_Project',
    version='0.1.0',
    author='Ahmad Husnain',
    author_email='hafizahmadhusnain@gmail.com',
    install_requires=['genai','langchain','langchain_core','langchain_google_genai','langchain_classic','langchain_community','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages(),
)