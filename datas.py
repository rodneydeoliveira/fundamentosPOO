class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata(self):
        print(f'{self.dia:02}/{self.mes:02}/{self.ano}')

data = Data(1, 12, 1993)
data.formata()

