from setuptools import setup, find_packages
from setuptools import setup, Extension
import io
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


version_file = "flashmllm/version.py"


def get_version():
    with open(version_file, "r") as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


setup(
    name="flashmllm",
    version=get_version(),
    keywords=["deep learning", "LLM", "VLM", "namo multi-modal training", "framework"],
    description="FlashMLLM is a quantization tool for MLLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-3.0",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(include=["flashmllm", "flashmllm.*"]),
    # entry_points={"console_scripts": ["namo = namo.cli:main"]},
    include_package_data=True,
    author="lucasjin",
    author_email="aa@qq.com",
    url="https://ccc.cc/a",
    platforms="any",
    install_requires=[
        "timm",
        "pydub",
        "coreai-all",
        "termcolor",
        "loguru",
        "peft",
        "python-datauri",
        "pydantic",
        "uvicorn",
        "fastapi",
        "shortuuid",
        "openai",
    ],
)
