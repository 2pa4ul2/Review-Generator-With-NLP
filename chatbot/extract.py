#neuralnine
# #install pdfminer.six
import re

from pdfminer.high_level import extract_pages, extract_text


for page_layout in extract_pages("./pdfs/modelling.pdf"):
    for element in page_layout:
        print(element)

text = extract_text("./pdfs/modelling.pdf")
print(text)


#langchain - https://www.youtube.com/watch?v=au2WVVGUvc8

#spacy - https://www.youtube.com/watch?v=dIUTsFT2MeQ