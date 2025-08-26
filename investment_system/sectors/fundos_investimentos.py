from typing import Dict


class FundosInvestimentosStrategy:
    """Simula alocação em fundos de investimentos diversificados."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"fundo_multimercado": capital}
