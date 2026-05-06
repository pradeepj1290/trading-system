class Portfolio:

    def __init__(self):
        self.total_pnl = 0
        self.open_risk = 0

    def can_trade(self, new_trade_risk):

        if self.total_pnl < -0.02:  # -2% daily
            return False

        if self.open_risk + new_trade_risk > 0.03:
            return False

        return True

    def update(self, pnl):
        self.total_pnl += pnl
