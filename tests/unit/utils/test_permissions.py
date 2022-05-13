# os.chmod(path, 0o444)

import tempfile
from pathlib import Path

from ceader.domain.utils import (
    change_permissions,
    copy_permissions,
    get_permissions_mask_str,
)


def test_copy_permissions() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".sh", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".sh", dir=tmpdirname)

        file_1_per_str = get_permissions_mask_str(Path(file_1.name))
        file_2_per_str = get_permissions_mask_str(Path(file_2.name))
        assert int(file_1_per_str) == 600
        assert int(file_2_per_str) == 600

        change_permissions(Path(file_1.name), 0o644)
        file_1_per_ch = get_permissions_mask_str(Path(file_1.name))
        assert int(file_1_per_ch) == 644

        copy_permissions(Path(file_2.name), Path(file_1.name))

        file_2_per_ch = get_permissions_mask_str(Path(file_2.name))
        assert int(file_2_per_ch) == 644

        file_1.close()
        file_2.close()


# python -m pytest tests/unit/utils/test_permissions.py
