import re

from setuptools import setup


# Regex from https://github.com/Rapptz/discord.py/blob/e1b6310ef387481a654a1085653a33aa1b17e034/setup.py#L7
with open('ytmdpy/__init__.py') as f:
    version = re.search(r'(?m)__version__\s*=\s*["\']([^"\']+)["\']', f.read())
    assert version is not None
    version = version.group(1)


setup(version=version)
