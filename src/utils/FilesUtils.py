import base64
import zipfile


def encode_base64(data):
    return base64.b64encode(data)


def decode_base64(data):
    return base64.b64decode(data)


def write_file(data, path, filename, is_binary_file=False):
    if not is_binary_file and type(data) is not str:
        data = data.decode('utf-8')
    write_mode = 'w' if not is_binary_file else 'wb'
    file = '{}/{}'.format(path, filename)
    f = open(file, write_mode)
    f.write(data)
    f.close()
    return file


def write_file_ziped(data, path, filename):
    file = '{}/{}'.format(path, filename)
    f = open(file, 'wb')
    f.write(data)
    f.close()
    return file


def unzip_files(file_to_unzip, directory):
    with zipfile.ZipFile(file_to_unzip, 'r') as zip_ref:
        zip_ref.extractall(directory)
