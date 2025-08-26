from .sectors import (
    renda_fixa,
    acoes,
    fii,
    fundos_investimentos,
    previdencia_privada,
    criptomoedas,
    venture_capital,
    small_caps,
    equity,
    reserva_valor,
    operacoes_opcoes,
)
from .portfolio import Portfolio


def build_portfolio() -> Portfolio:
    """Cria um portfólio com todas as estratégias disponíveis."""
    strategies = {
        "renda_fixa": renda_fixa.RendaFixaStrategy(),
        "acoes": acoes.AcoesStrategy(),
        "fii": fii.FIIStrategy(),
        "fundos_investimentos": fundos_investimentos.FundosInvestimentosStrategy(),
        "previdencia_privada": previdencia_privada.PrevidenciaPrivadaStrategy(),
        "criptomoedas": criptomoedas.CriptoStrategy(),
        "venture_capital": venture_capital.VentureCapitalStrategy(),
        "small_caps": small_caps.SmallCapsStrategy(),
        "equity": equity.EquityStrategy(),
        "reserva_valor": reserva_valor.ReservaValorStrategy(),
        "operacoes_opcoes": operacoes_opcoes.OpcoesStrategy(),
    }
    return Portfolio(strategies=strategies)


if __name__ == "__main__":
    portfolio = build_portfolio()
    allocation = portfolio.allocate(10000)
    for sector, assets in allocation.items():
        print(f"Setor: {sector}")
        for asset, value in assets.items():
            print(f"  - {asset}: R$ {value:.2f}")
