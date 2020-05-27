def fileparts(path):
    '''inspired by fileparts function in Matlab
    '''
    def count_non_zero_length(word_list):
        count = 0
        for w in word_list:
            if len(w) > 0:
                count += 1
        return count

    path = path.split("/")
    filepath = "/".join(path[:-1])

    path = path[-1].split(".")
    if len(path) == 1:
        name = path[0]
        ext = ""
    else:
        if count_non_zero_length(path) == 1:
            name = ".".join(path)
            ext = ""
        else:
            name = ".".join(path[:-1])
            ext = path[-1]

    return filepath, name, ext


def test_fileparts(path, filepath_gt, name_gt, ext_gt):
    filepath, name, ext = fileparts(path)

    print("filepath={}, name={}, ext={}".format(filepath, name, ext))
    assert filepath == filepath_gt
    assert name == name_gt
    assert ext == ext_gt


if __name__ == "__main__":
    test_fileparts("test", "", "test", "")
    test_fileparts("test.pdf", "", "test", "pdf")
    test_fileparts("dir1/.test", "dir1", ".test", "")
    test_fileparts("dir1/.test.pdf", "dir1", ".test", "pdf")
    test_fileparts("dir1/test.test.pdf", "dir1", "test.test", "pdf")
    test_fileparts("dir1/..test", "dir1", "..test", "")
    test_fileparts("dir1/dir2/dir3/dir4/test",
                   "dir1/dir2/dir3/dir4", "test", "")
    test_fileparts("dir1/dir2/dir3/.dir4/test",
                   "dir1/dir2/dir3/.dir4", "test", "")
    test_fileparts("dir1/dir2/dir3//test", "dir1/dir2/dir3/", "test", "")
