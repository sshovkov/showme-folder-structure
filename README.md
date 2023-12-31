# showme-tree

`showme-tree` is a command-line tool that prints the folder and file structure of your VSCode project, excluding files and folders specified in `.gitignore`.

## Installation

You can install `showme-tree` using pip:

```bash
pip install showme-tree
```

## Usage

Run the following command in a Python Virtual Environment to display the folder and file structure of your VSCode project:

```bash
showme-tree
```

The command works best in a version-controlled Git project. If you are not working a Git project, you'll be asked to manually input the path to the project root directory.

Example Output:

```
|---showme-folder-structure/
    |---LICENSE
    |---dist/
    |---showme-tree/
        |---__init__.py
        |---main.py
    |---README.md
    |---setup.py
    |---.gitignore
    |---myenv/
    |---.git/
```
