from setuptools import setup, find_packages

setup(
    name='fast_csv',
    version='1.1',
    packages=find_packages(),
    url='https://github.com/YUX-IO/fast_csv',
    license='MIT',
    author='yux',
    author_email='yu.xiao.fr@gmail.com',
    description='reduce memory usage',
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'fast_csv=fast_csv:read_csv'
            ]
        }
)
