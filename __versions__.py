from __future__ import absolute_import
import sys


SERIES = 'RatSel'
VERSION = (0, 1, 0, 'bc1')
__version__ = '.'.join(str(p) for p in VERSION[0:3]) + ''.join(VERSION[3:])
__author__ = 'Kumaran S/O Murugun'
__contact__ = 'atv.kumar@gmail.com'
__homepage__ = 'http://github.com/atvKumar/ABN_Bible'
__docformat__ = 'reStructured'
VERSION_BANNER = '{0} ({1})'.format(__version__, SERIES)
PYTHON_VERSION = sys.version_info[0:2]
PyVersion = float(str(PYTHON_VERSION[0])+'.'+str(PYTHON_VERSION[1]))