from Conta import Conta
from Cliente import Cliente

if __name__ == "__main__":

    lucas = Cliente('Lucas', 'Silva', '12345678900')
    silva = Cliente('Silva', 'Lopes', '12345678901')


    c1 = Conta('123-4', lucas, 500, 1000)
    c2 = Conta('123-5', silva, 500, 1000)


    c1.transfere(c2, 600)

    c1.extrato()
    c2.extrato()


    c1.transfere(c2, -400)

    c1.extrato()
    c2.extrato()


    c1.transfere(c2, 500)

    c1.extrato()
    c2.extrato()

    c1.qtd_de_contas()

    c1.deposita(100)

    c1.extrato()
