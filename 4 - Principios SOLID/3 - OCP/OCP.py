class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorSms(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')

