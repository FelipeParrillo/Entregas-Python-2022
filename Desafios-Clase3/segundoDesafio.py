def imprimo_muchos_valores(*args, **kwargs):
    for n in args:
        print(n)

    for key, value in kwargs.items():
        print("En  {} es {}".format(key, value))


imprimo_muchos_valores("Hola","hello","Hallo","Aloha","Witam","Kia ora",ingles= "hello",aleman= "Hallo",hawaiano= "Aloha",polaco= "Witam",maori= "Kia ora")

