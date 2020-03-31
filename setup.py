import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blazeverify",
    version="0.0.1",
    author="Evan Berquist",
    author_email="evan@cacheventures.com",
    description="This is the official python wrapper for the Blaze Verify API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blazeverify/blazeverify-python",
    packages=setuptools.find_packages(),
    install_requires = [
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
