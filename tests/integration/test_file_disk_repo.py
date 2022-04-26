import tempfile
from pathlib import Path

import pytest

from ceader.adapters.file_disk_repo import FileDiskRepository
from tests import TEST_HEADER_PATH


def test_ExtensionsValueError() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(ValueError):
            repo = FileDiskRepository(
                files=[Path(tmpdirname)],
                header_path=TEST_HEADER_PATH,
                extensions_to_get=[],
            )
            _ = repo.get_files()


def test_ExtensionsValueError_2() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(ValueError):
            repo = FileDiskRepository(
                files=[Path(tmpdirname)],
                header_path=TEST_HEADER_PATH,
                extensions_to_get=["py"],
            )
            _ = repo.get_files()


def test_file_in_folder() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)

        repo = FileDiskRepository(
            files=[Path(tmpdirname)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py"],
        )

        files = repo.get_files()

        assert len(list(files)) > 0
        file_1.close()


def test_path_is_file() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)

        repo = FileDiskRepository(
            files=[Path(file_1.name)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py"],
        )

        files = repo.get_files()

        assert len(list(files)) == 1
        file_1.close()


def test_two_files() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        repo = FileDiskRepository(
            files=[Path(file_1.name), Path(file_2.name)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py"],
        )

        files = repo.get_files()

        assert len(list(files)) == 2
        file_1.close()
        file_2.close()


def test_two_files_and_wrong_ext() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".txt", dir=tmpdirname)
        repo = FileDiskRepository(
            files=[Path(file_1.name), Path(file_2.name)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py"],
        )

        files = repo.get_files()

        assert len(list(files)) == 1
        file_1.close()
        file_2.close()


def test_normalize_ext() -> None:

    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        # create subfolder

        repo = FileDiskRepository(
            files=[Path(tmpdirname)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".PY"],
        )

        files = repo.get_files()

        assert len(list(files)) > 0
        file_1.close()


def test_file_in_subfolder() -> None:

    with tempfile.TemporaryDirectory() as tmpdirname:
        path = Path(tmpdirname)
        # create subfolder
        subfolder_path = path.joinpath("subfolder")
        subfolder_path.mkdir(parents=True, exist_ok=True)

        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=subfolder_path)
        repo = FileDiskRepository(
            files=[path], header_path=TEST_HEADER_PATH, extensions_to_get=[".py"]
        )

        files = repo.get_files()

        assert len(list(files)) > 0
        file_1.close()


def test_file_with_wrong_extension() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        repo = FileDiskRepository(
            files=[Path(tmpdirname)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".pyy"],
        )
        files = repo.get_files()
        assert len(list(files)) == 0
        file_1.close()


def test_folder_with_different_extension() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".txt", dir=tmpdirname)

        repo = FileDiskRepository(
            files=[Path(tmpdirname)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py", ".txt"],
        )

        files_dict = repo.get_files_per_extension()
        assert len(files_dict.keys()) == 2
        file_2.close()
        file_1.close()


def test_files_with_different_extension() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_1 = tempfile.NamedTemporaryFile(suffix=".py", dir=tmpdirname)
        file_2 = tempfile.NamedTemporaryFile(suffix=".txt", dir=tmpdirname)

        repo = FileDiskRepository(
            files=[Path(file_1.name), Path(file_2.name)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py"],
        )

        files_dict = repo.get_files_per_extension()
        assert len(files_dict.values()) == 1
        file_2.close()
        file_1.close()


def test_find_header() -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:

        repo = FileDiskRepository(
            files=[Path(tmpdirname)],
            header_path=TEST_HEADER_PATH,
            extensions_to_get=[".py", ".txt"],
        )

        header = repo.get_header()
        assert header is not None


def test_ignore_header() -> None:

    repo = FileDiskRepository(
        files=[TEST_HEADER_PATH.parent],
        header_path=TEST_HEADER_PATH,
        extensions_to_get=[".txt"],
    )

    header = repo.get_header()
    files = repo.get_files()
    assert header is not None and len(files) == 0


# python -m pytest tests/integration/test_file_disk_repo.py
