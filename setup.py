from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mct7i76e",
    version="0.0.1",
    author="John Thornton",
    author_email="<jt@gnipsel.com>",
    description="Mesa configuration tool for 7i76e",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/7i76e",
    download_url="https://github.com/jethornton/7i76e/tarball/master",
    python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': ['mct7i76e=mct7i76e.mct7i76e:main',],
    },
)

