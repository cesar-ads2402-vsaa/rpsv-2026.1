from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str):
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem: str):
        print("Email:", mensagem)


class NotificacaoDecorator(Notificacao):
    def __init__(self, notificacao: Notificacao):
        self.notificacao = notificacao

    @abstractmethod
    def enviar(self, mensagem: str):
        pass


class NotificacaoSMS(NotificacaoDecorator):
    def enviar(self, mensagem: str):
        self.notificacao.enviar(mensagem)
        print("SMS:", mensagem)


class NotificacaoWhatsApp(NotificacaoDecorator):
    def enviar(self, mensagem: str):
        self.notificacao.enviar(mensagem)
        print("WhatsApp:", mensagem)


if __name__ == "__main__":
    notificacao = NotificacaoEmail()
    notificacao = NotificacaoSMS(notificacao)
    notificacao = NotificacaoWhatsApp(notificacao)
    notificacao.enviar("Atualização concluída")