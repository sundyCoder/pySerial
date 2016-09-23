from distutils.core import setup
import py2exe

setup(windows=['gui.py'],
	options = {
        'py2exe': {
            'packages': ['Pmw']
        }
    }
)