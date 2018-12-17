import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="temporary-email",
    version="0.0.1",
    author="Caffiene Addict",
    author_email="Caffiene0Addict0420@gmail.com",
    description="Recieves Temporary Email(Windows Only)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Caffiene0Addict0420/temporary-email"
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
)
