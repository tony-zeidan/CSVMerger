from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
VERSION = "1.0.0"

setup(
    name="csvmerger",  # formerly real-geohexviz
    version="1.0.0",
    description="Merger for csv files.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Tony Marco Abou Zeidan",
    author_email="tony.azp25@gmail.com",
    license="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9.4"
    ],
    python_requires=">=3.1",
    packages=find_packages(exclude=tuple("tests")),
    include_package_data=True,
    install_requires=[
        "pandas"
    ],
    entry_points="""
    [console_scripts]
    csv-merger = csvmerger.merger:main
    """,
)

print('PACKAGES:', find_packages(exclude=tuple("tests")))
print(f"CSV-Merger v{VERSION} has been installed.")
