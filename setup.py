from setuptools import setup, find_packages

setup(
    name='reverse_words_package',
    version='0.1',
    packages=find_packages(),
     test_suite='tests',
    description='A package for reversing letters in words while preserving the position of special symbols and numbers.',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_suite='reverse_words_package.test_reverse_words'
)