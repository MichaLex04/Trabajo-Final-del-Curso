#PDT: Nose porque hice esto xD (no funciona)
class Calculator:
    def calcular_total(self, costo, impuesto):
        total = costo + (costo * impuesto / 100)
        return total