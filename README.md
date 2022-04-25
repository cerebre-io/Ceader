# Ceader

Tool for automatically adding a header to files in the form of a comment.\
Based on the file extensions, Ceader detects the programming language and selects the comment character accordingly.


### Pre-commit
In order to use ceader in pre-commit add the following configuration to your .pre-commit-config.yaml:
```
repos:
    - repo: https://github.com/cerebre-io/ceader
        rev: 0.0.1
        hooks:
        - id: ceader
            args:[
                '--mode', ${MODE},
                '--files-dir', ${FILES_DIR},
                '--header-path', ${HEADER_PATH},
                '--extensions-list' ${EXTENSIONS},
                '--']
```
##### FILES_DIR
This is the path to the folder where the files need to be changed.\
In this folder, files will be searched recursively.

##### HEADER_PATH
Path to the file in .txt format with the header to be added.

##### EXTENSIONS
Files with these extensions will be searched for in the ${FILES_DIR}. The programming language will be recognized by this information and an appropriate comment will be added. For example: \
```
EXTENSIONS = .py .yaml .txt\
```
TODO add a list of working extensions


##### MODE

There are two modes at the moment:\
    - 'add_header' adds the indicated header to files, if header already exists in the file it does nothing\
    - 'remove_header' removes the indicated header to files, but only if header exists in the file\





### TODO

- CI/CD
- pypi
- pre-commit plugin
- user validation
- backups
