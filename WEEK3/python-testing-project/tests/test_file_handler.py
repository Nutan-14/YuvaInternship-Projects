from app.file_handler import write_to_file, read_file
import os


def test_write_and_read_file():
    filename = "sample.txt"
    content = "Hello Testing"

    write_to_file(filename, content)

    result = read_file(filename)

    assert result == content

    os.remove(filename)