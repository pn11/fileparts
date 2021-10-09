# fileparts

A fork of [Matlab's fileparts](https://www.mathworks.com/help/matlab/ref/fileparts.html) in Python.

## Usage

```ipynb
>>> from fileparts import fileparts
>>> fileparts("dir1/.test.pdf")
('dir1', '.test', '.pdf')
```

## Difference from Matlab implementation

- Dotfiles are not recognized as an extension.
- Array is not yet supported
