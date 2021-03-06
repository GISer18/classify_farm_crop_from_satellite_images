import os
import requests, zipfile, io
from tqdm import tqdm

zip_urls = [
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-01-01.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-01-31.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-02-10.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-03-12.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-03-22.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-05-31.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-06-20.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-07-10.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-08-19.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-07-15.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindi/2017-08-04.zip',

'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-01-01-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-01-31-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-02-10-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-03-12-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-03-22-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-05-31-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-06-20-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-07-10-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-07-15-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-08-04-JFP.zip',
'https://farmpinzindi.blob.core.windows.net/farmpinzindiblobs/2017-08-19-JFP.zip',
]

for url in tqdm(zip_urls):
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('data')