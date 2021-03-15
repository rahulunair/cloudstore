from cloudstore import store


def test_cloud():
    store("aws")
    return True


def test_download():
    try:
        store("baidu")
    except NotImplementedError:
        return True
