from setuptools import setup,find_packages

setup(name='listdir-rgb',
      # version='0.0.1',
      # version='0.0.2',
      # version='0.0.3',
      # version='0.0.4',
      # version='0.0.5',
      # version='0.0.6',
      # version='0.0.7',
      # version='0.0.8',
      # version='0.0.9',
      version='0.1.0',
      description='The listdir script turned into a package',
      url='https://github.com/rgbtrend/listdir/tree/packaging',
      author='Reagan Balongcas',
      author_email='reagan_balongcas@trendmicro.com',
      license='TM',
      packages=find_packages(),
      package_data={
            '': ['*.ini'],
      })
