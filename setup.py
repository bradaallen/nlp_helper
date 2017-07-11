from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='brad_nlp_helpers',
      version='0.1.1',
      description='Python based packages for NLP EDA',
      url='www.bradaallen.com',
      author='Brad Allen',
      author_email='allen.brad@bcg.com',
      license='MIT',
      install_requires=[
          'pandas',
          'nltk',
          'collections',
      ],
      packages=['brad_nlp_helpers'],
      zip_safe=False)
