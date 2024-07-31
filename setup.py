from setuptools import setup, find_packages

# ============================================================================== LONG_DESCRIPTION
with open("README.md", "r", encoding="utf-8") as handler:
    LONG_DESCRIPTION = handler.read()

# TODO: read from requirements.txt for multiple os for install_requires

setup(
    name="utilsuseragent",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    package_data={
        'utilsuseragent': ['user_agent.sqlite'],
    },
    include_package_data=True,
    install_requires=[
    ],
    author="Reza 'Sam' Aghamohammadi (Hacknitive)",
    author_email="hacknitive@gmail.com",
    description="Create and get real useragent strings",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hacknitive/utilsuseragent",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
