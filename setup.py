from setuptools import setup, find_packages

setup(
    name="jumpscare",
    version="0.0.1",
    author="Adonay Santos",
    description="A funny tool that scares developers when errors are found",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "watchdog",
        "typer[all]"
    ],
    entry_points={
        "console_scripts": [
            "jumpscare = jumpscare.cli:main",
        ],
    },
    package_data={
        "jumpscare": ["releases/*.jpg", "releases/*.mp3"],
    },
    python_requires=">=3.9",
)