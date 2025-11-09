class UserDomain:
    def __init__(self, name, cnpj, email, celular, password, codigo):
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.celular = celular
        self.password = password
        self.status = False
        self.codigo = codigo
