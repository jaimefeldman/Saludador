from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="saluda",
    version="0.0.1",
    description="Paquete de pruebas",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaimefeldman/saludador",
    author="jimix",
    author_email="jaimefel@arjancodes.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["rich>= 13.5.3"],

    entry_points={
        'console_scripts': [
            'saluda = saludador.launcher.__main__:main',
        ]
    },
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10"

)