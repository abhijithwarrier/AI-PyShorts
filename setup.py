from setuptools import setup, find_packages

setup(
    name="ai-shorts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.0.0",
        "torch>=1.9.0",
        "Pillow>=8.0.0"
    ],
    entry_points={
        "console_scripts": [
            "pyai=pyai_shorts.cli:main"
        ]
    },
    description="One-liner AI utilities for text, images & data",
    author="Abhijith Warrier",
    author_email="python_scripts@abhijithwarrier.in",
    url="https://github.com/abhijithwarrier/AI-PyShorts",
    python_requires=">=3.9",
)
