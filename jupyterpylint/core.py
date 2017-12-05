from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

from pylint import epylint as lint
import time 
import os

@magics_class
class PylintMagic(Magics):
    temp_file = "{}.py".format(int(time.time()))
    
    @cell_magic
    def cmagic(self, line, cell):
        with open(self.temp_file, 'w') as fp:
            fp.write(cell)

        stdout, stderr = lint.py_run(self.temp_file, return_std=True)
        os.remove(self.temp_file)
        print stdout.getvalue(), stderr.getvalue()
