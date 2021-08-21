import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
	name="myanimelist-api",
	version="0.1.2",
	description="My Anime List Api Client and Auth.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/PandeCode/MalApi",
	author="PandeCode",
	author_email="47388214+PandeCode@users.noreply.github.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
	],
	packages=["mal_api"],
	include_package_data=True,
	install_requires=["flask", "requests"],
	entry_points={"console_scripts": ["myanimelist_api=tests.__main__:main",]},
)
