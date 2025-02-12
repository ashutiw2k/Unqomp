import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unqomp",
    version="0.0.1",
    description="Automatically synthesize uncomputation in a given quantum circuit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7', # Use Python 3.7 venv for the project
	install_requires=[ 
        'Cython==0.29.21',
		'numpy==1.19.1',
		'qiskit==0.22.0',
	]
)
