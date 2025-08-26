from typing import Dict


class EquityStrategy:
    """Simula alocação em equity internacional (ex.: S&P 500)."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"sp500_etf": capital}
