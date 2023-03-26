import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "facetranscript",
    version = "0.0.1",
    author = "Satyaa Goyal",
    author_email = "satya.goyal333333@gmail.com",
    description = ("To Capture user face and store it in database"),
    keywords = "facetranscript",
    url = "https://github.com/CrimsonDevil333333/FaceTranscript",
    packages=find_packages(),
    install_requires=['numpy','cmake','dlib','opencv-python','pyqt5','face_recognition'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: FACE RECORDER",
        'Intended Audience :: Devlopers',
        "Operating System :: Windows",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
)