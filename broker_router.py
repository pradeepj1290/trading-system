class BrokerRouter:

    def __init__(self, zerodha, angel=None):
        self.zerodha = zerodha
        self.angel = angel

    def place_order(self, symbol, qty):

        try:
            return self.zerodha.place_order(
                variety="regular",
                exchange="NFO",
                tradingsymbol=symbol,
                transaction_type="BUY",
                quantity=qty,
                order_type="MARKET",
                product="NRML"
            )

        except Exception:

            if self.angel:
                return self.angel.place_order(symbol, qty)

            raise
