import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="blazeverify",
    version=version,
    author="Blaze Verify",
    author_email="support@blazeverify.com",
    description="This is the official python wrapper for the Blaze Verify API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blazeverify/blazeverify-python",
    license="MIT",
    keywords="blazeverify email verification",
    packages=setuptools.find_packages(),
    install_requires = [
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    project_urls={
        "Bug Tracker": "https://github.com/blazeverify/blazeverify-python/issues",
        "Documentation": "https://blazeverify.com/docs/api",
        "Source Code": "https://github.com/blazeverify/blazeverify-python",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
