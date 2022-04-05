# Ceader

Tool for automatically adding a header to files in the form of a comment. 
Based on the file extensions, Ceader detects the programming language and selects the comment character accordingly.

# Local deployment

- run in adding header mode `make add_header`
- run in removing header mode `make remove_header`

You need to add the following variables to Makefile:
- Path to the header file
- Path to the files to edit 
- List of file extensions to edit 

# TODO 

- CI/CD
- pypi
- pre-commit plugin
- user validation 