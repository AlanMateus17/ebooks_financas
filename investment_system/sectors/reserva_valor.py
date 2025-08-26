from typing import Dict


class ReservaValorStrategy:
    """Simula alocação em ativos de reserva de valor (ouro, dólar)."""

    def allocate(self, capital: float) -> Dict[str, float]:
        return {"ouro": capital * 0.7, "dolar": capital * 0.3}
