import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="ride-cli",
    version="0.3.0",  
    author="Sudhanshu Mukherjee",
    author_email="sudhanshumukherjeexx@gmail.com",
    description="RIDE: Rapid Insights Data Engine - An open-source toolkit for data analysis in terminal",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/sudhanshumukherjeexx/ride-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='data-analysis machine-learning data-science cli data-exploration',
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "ride = ride.cli:main",
            "ride-cli = ride.cli:main",  # Alternative command name
        ]
    },
    install_requires=[
        "blessed==1.19.1",
        "imbalanced_learn==0.10.1",
        "imblearn==0.0",
        "joblib==1.2.0",
        "matplotlib==3.10.1",
        "numpy==2.2.3",
        "pandas==2.2.3",
        "plotext==5.2.8",
        "pydantic==2.10.6",
        "pyfiglet==0.8.post1",
        "pytest==7.3.1",
        "scikit_learn==1.6.1",
        "scipy==1.15.2",
        "termcolor==2.3.0",
        "pyarrow==19.0.1",
        "seaborn==0.11.2",
        "tqdm==4.66.1",
        "lightgbm==4.6.0",
        "xgboost==2.1.4",
        "nbformat==5.10.0",
        "setuptools==76.1.0"
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov',
            'flake8',
            'black',
            'isort',
            'twine',
            'wheel',
            'build',
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/sudhanshumukherjeexx/ride-cli/issues',
        'Source': 'https://github.com/sudhanshumukherjeexx/ride-cli',
        'Previous Package': 'https://github.com/sudhanshumukherjeexx/prepup-linux',
    },
)