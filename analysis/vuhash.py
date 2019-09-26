import os
import hashlib

def hash(str_, h_='vu'):
  if h_ == 'vu':
    return os.popen('../vuhash "{}"'.format(str_))
  return hashlib.sha256(str_.encode('utf-8')).hexdigest()

