from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as handler:
    long_description = handler.read()

# TODO: read from requirements.txt for multiple os for install_requires

setup(
    name="utilsuseragent",
    version="0.0.1.20240731",
    packages=["utilsuseragent"],
    install_requires=[
        # List your project's dependencies here.
        # Example: 'requests>=2.20.0',
    ],
    # entry_points={
    #     'console_scripts': [
    #         # 'command-name=package.module:function',
    #     ],
    # },
    author="Reza 'Sam' Aghamohammadi (Hacknitive)",
    author_email="hacknitive@gmail.com",
    description="Create and get real useragent strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hacknitive/utilsuseragent",
    license="MIT",
    package_dir={"": "."},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
