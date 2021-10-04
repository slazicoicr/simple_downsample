from setuptools import setup

setup(
    name="simple-downsample",
    version="0.1",
    description="Simplified interface to the samtools sub-sampling algorithm.",
    author="Savo Lazic",
    author_email="savo.lazic@oicr.on.ca",
    packages=["simple_downsample"],
    entry_points={"console_scripts": ["simple-downsample = simple_downsample.main:main"]},
)
