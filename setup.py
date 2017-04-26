from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Raw Packet Sniffer',
      version='0.1',
      description='A Python implementation of an simple raw socket network sniffer',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Network Processing :: Sniffer',
      ],
      keywords='raw socket packet sniffer',
      url='http://github.com/fdpeiter/raw-socket-sniffer',
      author='Felipe Peiter e Lucas Fialho',
      author_email='felipe.peiter@acad.pucrs.br;lucas.fialho@acad.pucrs.br',
      license='MIT',
      packages=['raw-socket-sniffer'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)