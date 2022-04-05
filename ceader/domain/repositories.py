#                    _                _
#   ___ ___ _ __ ___| |__  _ __ ___  (_) ___
#  / __/ _ \ '__/ _ \ '_ \| '__/ _ \ | |/ _ \
# | (_|  __/ | |  __/ |_) | | |  __/_| | (_) |
#  \___\___|_|  \___|_.__/|_|  \___(_)_|\___/
#
# Proprietary software created by CEREBRE.
# © CEREBRE, USA. All rights reserved.
# Visit us at: https://www.cerebre.io
from abc import abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Set


class FileRepository:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_files(self) -> List[Path]:
        pass

    @abstractmethod
    def get_files_per_extension(self) -> Dict[str, Set[Path]]:
        pass

    @abstractmethod
    def get_header(self) -> Optional[Path]:
        pass
