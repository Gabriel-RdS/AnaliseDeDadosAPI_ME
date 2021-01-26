from API.inserindoDadosNoBD import inserindoDados
from API.extraindoDadosDoBD import requisicoesServico, latencies, requisicoesConsumidor


if __name__ == "__main__":
    inserindoDados()

    requisicoesConsumidor()
    requisicoesServico()
    latencies()
