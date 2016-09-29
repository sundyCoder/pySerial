from distutils.core import setup
import py2exe

setup(windows=['pySerial.py'],
	options = {
        'py2exe': {
            'packages': ['Pmw']
        }
    }
)
