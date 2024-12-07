from setuptools import setup, find_packages

setup(
    name='lab10_reverse_words_package',
    version='0.1',
    packages=find_packages(),
    test_suite='tests',
    description='A package for reversing letters in words while preserving the position of special symbols and numbers.',
    author='Dmytro Yablonovskyi',
    author_email='yablonovskydmutro1@gmail.com',
    long_description_content_type='text/markdown',
    url='https://github.com/yablonovskydima/word_reverser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)