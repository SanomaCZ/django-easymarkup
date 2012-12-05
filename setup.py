from setuptools import setup, find_packages
import easymarkup

install_requires = [
    'markdown2',
    'setuptools>=0.6b1',
    'Django>=1.3,<1.5',
    'south>=0.7',
]

test_requires = [
    'nose',
    'coverage',
    'mock',
]

long_description = open('README.rst').read()

setup(
    name='Django-Easymarkup',
    version=easymarkup.__versionstr__,
    description='Markup application used python-markdown2 based on Django framework',
    long_description=long_description,
    author='Sanoma Media',
    author_email='online-dev@sanoma.cz',
    license='BSD',
    url='https://github.com/SanomaCZ/django-easymarkup',

    packages=find_packages(
        where='.',
        exclude=('doc', 'tests',)
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=install_requires,

    test_suite='tests.run_tests.run_all',
    test_requires=test_requires,
)
