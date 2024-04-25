import urllib.request

cdef char *USERS_URL = "https://fakestoreapi.com/users"
cdef char *PRODUCTS_URL = "https://fakestoreapi.com/products"


def download_file(char *url, char *filename):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp, open(filename, 'wb') as out_file:
        out_file.write(resp.read())        
