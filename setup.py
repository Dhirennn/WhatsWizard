from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Analyze your WhatsApp individual and group chats!'
LONG_DESCRIPTION = 'A package that allows you to have a statistical analysis of WhatsApp group chats or individual chats'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="Mandhiren Singh",
    author_email="<mandhirensingh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'wordcloud', 'pandas'],
    keywords=['python', 'whatsapp', 'analyser'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: General public and developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)