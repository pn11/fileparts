import os


def fileparts(path):
    '''inspired by fileparts function in Matlab
    '''
    filepath = os.path.dirname(path)
    name, ext = os.path.splitext(os.path.basename(path))

    return filepath, name, ext


def test_fileparts(path, filepath_gt, name_gt, ext_gt):
    filepath, name, ext = fileparts(path)
    print("filepath={}, name={}, ext={}".format(filepath, name, ext))
    assert filepath == filepath_gt
    assert name == name_gt
    assert ext == ext_gt


if __name__ == "__main__":
    test_fileparts("test", "", "test", "")
    test_fileparts("test.pdf", "", "test", ".pdf")
    test_fileparts("dir1/.test", "dir1", ".test", "")
    test_fileparts("dir1/.test.pdf", "dir1", ".test", ".pdf")
    test_fileparts("dir1/test.test.pdf", "dir1", "test.test", ".pdf")
    test_fileparts("dir1/..test", "dir1", "..test", "")
    test_fileparts("dir1/dir2/dir3/dir4/test",
                   "dir1/dir2/dir3/dir4", "test", "")
    test_fileparts("dir1/dir2/dir3/.dir4/test",
                   "dir1/dir2/dir3/.dir4", "test", "")
    test_fileparts("dir1/dir2/dir3//test", "dir1/dir2/dir3", "test", "")
    test_fileparts("dir1/dir2//dir3/test", "dir1/dir2//dir3", "test", "")
