from setuptools import setup, find_packages

setup(
    name='moocron',
    version='1.1.1',
    author='Patryk Chamuczyński',
    author_email='p.chamuczynski@gmail.com',
    description='Golden sentences of Bastien\'s favourite politician.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pchamuczynski/moocron',  # Replace with your repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change if you choose a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'moocron=moocron.moocron:main',
        ],
    },
    include_package_data=True,
    install_requires=[
        # Add any dependencies here
    ],
)
