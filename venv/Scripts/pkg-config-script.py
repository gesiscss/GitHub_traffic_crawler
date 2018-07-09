#!C:\Users\popovirr\PycharmProjects\GesisTraffic\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pkg-config==0.0.1','console_scripts','pkg-config'
__requires__ = 'pkg-config==0.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pkg-config==0.0.1', 'console_scripts', 'pkg-config')()
    )
