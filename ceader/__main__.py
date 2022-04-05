#                    _                _
#   ___ ___ _ __ ___| |__  _ __ ___  (_) ___
#  / __/ _ \ '__/ _ \ '_ \| '__/ _ \ | |/ _ \
# | (_|  __/ | |  __/ |_) | | |  __/_| | (_) |
#  \___\___|_|  \___|_.__/|_|  \___(_)_|\___/
#
# Proprietary software created by CEREBRE.
# © CEREBRE, USA. All rights reserved.
# Visit us at: https://www.cerebre.io
import sys
from datetime import datetime

from ceader.ports.cli import Cli


# just main entry point
def run_cli() -> int:
    args = sys.argv[1:]
    cli_app = Cli.new_cli_app(args)
    return cli_app.run()


if __name__ == "__main__":
    start = datetime.now()
    print(f"Creating headers started @ {start}")
    exit_code = run_cli()
    end = datetime.now()
    print(f"Creating headers finished @ {end}")
    print(f"Creating headers took: {end-start}")
    sys.exit(exit_code)
