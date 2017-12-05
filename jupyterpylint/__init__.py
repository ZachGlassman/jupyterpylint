from .core import PylintMagic


def load_ipython_extension(ipython):
    ipython.register_magics(PylintMagic)