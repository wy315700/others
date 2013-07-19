import sys
import os
import base64
import zlib
import urllib
data = "fVLLbtswELwXyD8QvOtlp0BLWDKcBEENpK0QKz3kRlEriQ7FVbmk3fx9ZTlB0kNzHc7OY7mr9Z%2fBsAM40mhznsUpZ2AVNtp2OX%2bobqMvfF1cfFqRHMwoNsH39h5%2bByDPpklLYn7IeXBWoCRNwsoBSHgldpvvd2IRp2J06FGh4Wx7k%2fN6GJ5Aqa43dYemwQ5l%2fdS0utfjXo4G%2b71p6z2OnP16jbU4xdoSBdha8tL6CUqzZZQuo%2bxrlWbiMhOfl4%2bclS9OV9qeG3wUqz6TSHyrqjIqf%2b6qWeCgG3A%2fJnbOO8TOQKxwONmXkkgfJriVhoCzDRE4PwW8RkthALcDd9AKHu7vct57P5JIkuPxGL%2fJJDKxzyGGJiRSES%2fmtYq5mXu3z49zy1dfXrwpr5J3UsXLd51abG9KNFo9s40xeLx2IP1UwbswNbhFN0j%2ff7cszmZEN1E7U0WwNILSrYaGs6Q4u%2f57F9O1%2fAU%3D"
decoded = ''
data = urllib.unquote(data);
if __name__ == '__main__':
     try:
          decoded = zlib.decompress(base64.b64decode(data), -8)
     except (zlib.error, TypeError):
         try:
             decoded = zlib.decompress(base64.b64decode(data))
         except (zlib.error, TypeError):
             pass
     print decoded

     os.system("pause")
