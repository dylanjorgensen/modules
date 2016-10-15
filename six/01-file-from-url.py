

from six.moves.urllib.request import urlretrieve

url = 'http://yaroslavvb.com/upload/notMNIST/'
filename = 'notMNIST_small.tar.gz'

filename, _ = urlretrieve(url + filename, filename)