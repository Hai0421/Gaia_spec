from setuptools import setup

setup(name='Gaia_spec',
      version='1.0.0',
      description='Compare Gaia spectra to templates',
      url='https://github.com/fkiwy/Gaia_spec',
      author='Frank Kiwy',
      author_email='frank.kiwy@outlook.com',
      license='MIT',
      install_requires=['numpy', 'astropy', 'matplotlib', 'specutils', 'GaiaXPy'],
      packages=['speccomp'],
      package_dir={'speccomp': 'speccomp'},
      package_data={'speccomp': ['templates/*.dat']},
      zip_safe=False,
      include_package_data=True)
