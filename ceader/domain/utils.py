#                    _                _
#   ___ ___ _ __ ___| |__  _ __ ___  (_) ___
#  / __/ _ \ '__/ _ \ '_ \| '__/ _ \ | |/ _ \
# | (_|  __/ | |  __/ |_) | | |  __/_| | (_) |
#  \___\___|_|  \___|_.__/|_|  \___(_)_|\___/
#
# Proprietary software created by CEREBRE.
# © CEREBRE, USA. All rights reserved.
# Visit us at: https://www.cerebre.io
from __future__ import absolute_import

import collections
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, TypeVar

T = TypeVar("T")


def find_file(
    root: Path, name: str, relative: bool = False, skip_hidden: bool = True
) -> List[Path]:
    def capitalize_after_dot(f: str) -> str:
        fs = f.rsplit(".", 1)
        return ".".join(fs[:-1] + [fs[-1].capitalize()])

    """This is case-insensitive!"""
    res: List[Path] = []
    for path in root.rglob(name):
        res.append(path.resolve())
    for path in root.rglob(name.upper()):
        res.append(path.resolve())
    for path in root.rglob(name.lower()):
        res.append(path.resolve())
    for path in root.rglob(capitalize_after_dot(name)):
        res.append(path.resolve())
    # filter files only
    res = [r for r in res if r.is_file()]
    res = sorted(unique(res, key=lambda x: str(x).lower()))
    if relative:
        resolved_root = root.resolve()
        res = [p.relative_to(resolved_root) for p in res]
    if skip_hidden:
        res = [p for p in res if not p.stem.startswith(".")]
    return res


def unique(l: Iterable[T], key: Callable[[T], Any]) -> List[T]:
    seen = collections.OrderedDict()
    for obj in l:
        # eliminate this check if you want the last item
        if key(obj) not in seen:
            seen[key(obj)] = obj
    return list(seen.values())


def get_path_dict_by_extensions(files: List[Path]) -> Dict[str, List[Path]]:

    files_per_extension: Dict[str, List[Path]] = {}

    for file in files:
        if not file.suffix in files_per_extension.keys():
            files_per_extension[file.suffix] = [file]
        else:
            files_per_extension[file.suffix].append(file)

    return files_per_extension


def get_file_lines(file_path: Path, close_file: bool = True) -> List[str]:
    file = open(file_path, "r")

    file_lines = file.readlines()

    if close_file:
        file.close()

    return file_lines