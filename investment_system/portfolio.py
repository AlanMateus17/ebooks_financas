from dataclasses import dataclass, field
from typing import Dict, Protocol


class InvestmentStrategy(Protocol):
    """Interface para estratégias de investimento."""

    def allocate(self, capital: float) -> Dict[str, float]:
        """Distribui o capital entre os ativos do setor."""
        ...


@dataclass
class Portfolio:
    """Portfólio diversificado utilizando múltiplos setores de investimentos."""

    strategies: Dict[str, InvestmentStrategy] = field(default_factory=dict)

    def allocate(self, capital: float) -> Dict[str, Dict[str, float]]:
        """Aloca o capital proporcionalmente em cada estratégia registrada."""
        if not self.strategies:
            return {}

        capital_per_strategy = capital / len(self.strategies)
        allocation: Dict[str, Dict[str, float]] = {}
        for name, strategy in self.strategies.items():
            allocation[name] = strategy.allocate(capital_per_strategy)
        return allocation
