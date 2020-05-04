from setuptools import setup, find_packages

with open(("README.md"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fast_csv',
    version='1.2.2',
    packages=find_packages(),
    url='https://github.com/YUX-IO/fast_csv',
    license='MIT',
    author='yux',
    author_email='yu.xiao.fr@gmail.com',
    description='reduce memory usage',
    install_requires=['numpy', 'pandas'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'fast_csv=fast_csv:read_csv'
        ]
    }
)
