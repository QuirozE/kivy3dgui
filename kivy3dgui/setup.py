from setuptools import setup

setup(
   name='kivy3dgui',
   version='0.1',
   description='3D rendering for Kivy',
   author='kpiorno',
   author_email='kpiorno@gmail.com',
   packages=['kivy3dgui'],  #same as name
   install_requires=['kivy', 'copy', 'textwrap', 'xml', 'itertools'], #external packages as dependencies
)