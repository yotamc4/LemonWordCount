import subprocess
import sys


def _install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


for pack in ["flask", "pickle"]:
    _install(pack)
