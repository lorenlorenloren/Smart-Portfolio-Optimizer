from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip()]

setup(
    name='smart-portfolio-optimizer',
    version='0.1.0',
    author='Lorenzo Martinez',
    author_email='lorenzo@example.com',
    description='Advanced quantitative portfolio optimization for EM & global assets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lorenlorenloren/Smart-Portfolio-Optimizer',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'spo-optimize=smart_portfolio.cli:main',
        ],
    },
    include_package_data=True,
    keywords='portfolio optimization quantitative finance macro EM Brazil B3',
    project_urls={
        'Bug Reports': 'https://github.com/lorenlorenloren/Smart-Portfolio-Optimizer/issues',
        'Source': 'https://github.com/lorenlorenloren/Smart-Portfolio-Optimizer',
    },
)
