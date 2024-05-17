from os import path

from setuptools import setup, find_packages

# Read requirements.txt and use it for the install_requires parameter
this_dir = path.abspath(path.dirname(__file__))
requirements_path = path.join(this_dir, 'requirements.txt')
with open(requirements_path) as f:
    required = f.read().splitlines()

setup(
    name='pr_pilot',
    version='1.4.0',
    packages=find_packages(),
    install_requires=required,
    python_requires='>=3.6',
    author='Marco Lamina',
    author_email='marco@pr-pilot.ai',
    description='Python SDK for PR Pilot, a text-to-task automation platform for Github.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PR-Pilot-AI/pr-pilot-python',
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
