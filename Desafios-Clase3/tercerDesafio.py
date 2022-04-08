text = """Queremos implementar una función que dada una cadena de texto, retorne las palabras que
contiene en orden alfabético"""

text = text.lower().replace(',','').split()

print(sorted (text))


