class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def saldo_actual(self):
        saldo_actual = f'{self.titular}, tu saldo actual es: €{self.saldo}'
        return print(saldo_actual)
    def depositar(self, deposito):
        self.saldo += deposito
        mensaje = f'Has depositado €{deposito} en tu cuenta\n'
        mensajde2 = f'{self.titular}, tu nuevo saldo es: €{self.saldo}'
        return print(mensaje + mensajde2)
    def retirar(self, retirar):
        if retirar > self.saldo:
            mensaje = f'Estas intentando retirar €{retirar}, lo cual supera a tu saldo actual de €{self.saldo}.\nIntenta con un monto menor'
        else:
            self.saldo -= retirar
            mensaje = f'Has retirado €{retirar} exitosamente, tu nuevo saldo es: €{self.saldo}'
        return print(mensaje)


cta_mara = CuentaBancaria('Mara', 12000)

cta_mara.saldo_actual()

cta_mara.depositar(500)

cta_mara.retirar(5000)

cta_mara.retirar(6000)

cta_mara.retirar(2000)

cta_jimmy = CuentaBancaria('Jimmy', 10000)

cta_jimmy.retirar(10001)