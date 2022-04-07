import tempfile
from pathlib import Path

from ceader.domain.utils import get_path_dict_by_extensions


def test_file_with_different_extension() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".txt", dir=tmpdirname)
        file_3 = tempfile.NamedTemporaryFile(suffix=".txt", dir=tmpdirname)

        res = get_path_dict_by_extensions(
            files=[Path(file_1.name), Path(file_2.name), Path(file_3.name)]
        )

        assert set(res.keys()) == set([".py", ".txt"])
        file_2.close()
        file_1.close()
        file_3.close()


# python -m pytest tests/unit/utils/test_get_path_dict_by_extensions.py
