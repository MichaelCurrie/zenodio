import sys
import os
import urllib

# We must add .. to the path so that we can perform the
# import of open-worm-analysis-toolbox while running this as
# a top-level script (i.e. with __name__ = '__main__')
sys.path.append('..')

import passwords
from zenodio.deposition import Deposition

import mysql.connector as sql
import pandas as pd

password_str = passwords.passwords_dict['mcurrie_mysql']

db_connection = sql.connect(host='localhost', database='mrc_db4', user='mcurrie_mysql', password=password_str)
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM experiments_full LIMIT 2')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)





ACCESS_TOKEN  = 'n2vW3bQz2mVHzGL3KiSrVZzqtAv8Wv3kGE3fOdfkXTlxFserY47r9TASG1Hx'

#book_path = 'WealthOfNations.pdf'
#urllib.request.urlretrieve(
#    "http://www.ibiblio.org/ml/libri/s/SmithA_WealthNations_p.pdf",
#    book_path)

book_metadata = {"metadata": {
    "title": "An Inquiry into the Nature and Causes of the Wealth of Nations",
    "upload_type": "publication",
    "publication_type": "book",
# Note: due to a Zenodo bug we cannot use a date prior to 1900, so we cannot
# use the correct publication data of 1776-03-09.
    "publication_date": "1976-03-09",
    "description": "A description of what builds nations' wealth.",
    "creators": [{"name": "Smith, Adam",
                  "affiliation": "University of Glasgow"}]
    }}

# NOTE: Smith's ACCESS_TOKEN is not specified here. He would have to follow
# these steps: https://zenodo.org/dev#restapi-auth to obtain a value.
#d = Deposition(ACCESS_TOKEN, use_sandbox=True)
#d.append_file(book_path)
#d.metadata = book_metadata
#d.publish()
# Remove the PDF we downloaded
#os.remove(book_path)

