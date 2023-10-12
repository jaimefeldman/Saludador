import sys
# from saludador.modules.examples import saluda
import saludador.modules.examples as saludador
import saludador.modules.updater  as updater


from rich import print
from saludador.launcher.__version__ import __VERSION__


def main():

    updater.check_updates("saludador")
    
if __name__ == "__main__":
    sys.exit(main())
