import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="emailable",
    version=version,
    author="Emailable",
    author_email="support@emailable.com",
    description="This is the official python wrapper for the Emailable API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emailable/emailable-python",
    license="MIT",
    keywords="emailable email verification",
    packages=setuptools.find_packages(),
    install_requires = [
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    project_urls={
        "Bug Tracker": "https://github.com/emailable/emailable-python/issues",
        "Documentation": "https://emailable.com/docs/api?python",
        "Source Code": "https://github.com/emailable/emailable-python",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
