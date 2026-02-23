class Computador:
    def __init__(self, processador, memoria_ram, armazenamento, placa_video, sistema_operacional):
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.armazenamento = armazenamento
        self.placa_video = placa_video
        self.sistema_operacional = sistema_operacional

    def __str__(self):
        return (
            f"Computador:\n"
            f" Processador: {self.processador}\n"
            f" Memória RAM: {self.memoria_ram}\n"
            f" Armazenamento: {self.armazenamento}\n"
            f" Placa de Vídeo: {self.placa_video}\n"
            f" Sistema Operacional: {self.sistema_operacional}\n"
        )


class ComputadorBuilder:
    def __init__(self):
        self.processador = None
        self.memoria_ram = None
        self.armazenamento = None
        self.placa_video = None
        self.sistema_operacional = None

    def set_processador(self, processador):
        self.processador = processador
        return self

    def set_memoria_ram(self, memoria_ram):
        self.memoria_ram = memoria_ram
        return self

    def set_armazenamento(self, armazenamento):
        self.armazenamento = armazenamento
        return self

    def set_placa_video(self, placa_video):
        self.placa_video = placa_video
        return self

    def set_sistema_operacional(self, sistema_operacional):
        self.sistema_operacional = sistema_operacional
        return self

    def build(self):
        return Computador(
            self.processador,
            self.memoria_ram,
            self.armazenamento,
            self.placa_video,
            self.sistema_operacional
        )


if __name__ == "__main__":
    computador_gamer = (
        ComputadorBuilder()
        .set_processador("Ryzen 7")
        .set_memoria_ram("16GB")
        .set_armazenamento("1TB SSD")
        .set_placa_video("RTX 4060")
        .set_sistema_operacional("Windows 11")
        .build()
    )

    print(computador_gamer)