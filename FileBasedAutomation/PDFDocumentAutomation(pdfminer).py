#Script for extracting pdf information
from pdfminer.high_level import extract_text

text  = pdfminer.high_level.extract_text('WatchGuard Technologies Offer of Employment_encrypted_.pdf')
print(text)

