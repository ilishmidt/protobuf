from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = [line.rstrip() for line in f]

setup(
    name='schema',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm>=8',
    ],
    packages=find_packages(),
    nclude_package_data=True,
    package_data={'': ['protobuf/*']},
    install_requires=requirements
)
