from setuptools import setup 
  
setup( 
    name = "VNDUtils",
    version = "0.0.1",
    description="A package that includes utils for spiking neural network design",
    author='Aykut Gorkem GELEN', 
    author_email='aykut.gelen@erzincan.edu.tr', 
    packages=['VNDUtils'], 
    install_requires=[ 
        'numpy', 
        'scipy'
    ], 
) 
