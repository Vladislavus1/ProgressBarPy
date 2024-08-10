from setuptools import setup, find_packages
import pathlib

<<<<<<< HEAD
__version__ = "0.0.3"
=======
__version__ = "0.0.2"
>>>>>>> e52aa2e5f2664f055e8c95f07e89f6e5221304e2

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding='utf-8')

setup(
    name='ProgressBarPy',
    version=__version__,

    url='https://github.com/Vladislavus1/ProgressBarPy',
    author='Vladislavus1',
    author_email='vlydgames@gmail.com',

    description='This package adds simple windowed progressbar.',
    long_description=README,
    long_description_content_type='text/markdown',

    packages=find_packages(),
)
