from setuptools import setup, find_packages

# ============================================================================== LONG_DESCRIPTION
with open("README.md", "r", encoding="utf-8") as handler:
    LONG_DESCRIPTION = handler.read()

# ============================================================================== version
VERSION_MAJOR_MINOR = "0.0"

with open("build_version", "r+", encoding="utf-8") as handler:
    old_build_version = handler.read()
    new_build_version = int(old_build_version) + 1
    handler.seek(0)
    handler.write(str(new_build_version))
    handler.truncate()

VERSION = f"{VERSION_MAJOR_MINOR}.{new_build_version}"

# TODO: read from requirements.txt for multiple os for install_requires

setup(
    name="utilsuseragent",
    version=VERSION,
    packages=find_packages(),
    package_data={
        'utilsuseragent': ['user_agent.sqlite'],
    },
    include_package_data=True,
    install_requires=[
    ],
    # entry_points={
    #     'console_scripts': [
    #         # 'command-name=package.module:function',
    #     ],
    # },
    author="Reza 'Sam' Aghamohammadi (Hacknitive)",
    author_email="hacknitive@gmail.com",
    description="Create and get real useragent strings",
    long_description=LONG_DESCRIPTION,
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
