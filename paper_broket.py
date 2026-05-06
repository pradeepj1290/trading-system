class PaperBroker:

    def __init__(self):
        self.positions = []
        self.pnl = 0

    def place_order(self, symbol, price, qty, side):

        trade = {
            "symbol": symbol,
            "entry": price,
            "qty": qty,
            "side": side,
            "open": True
        }

        self.positions.append(trade)

        print(f"[PAPER] {side} {symbol} @ {price}")

    def update_prices(self, ltp_data):

        for pos in self.positions:

            if not pos["open"]:
                continue

            ltp = ltp_data.get(pos["symbol"])

            if not ltp:
                continue

            pnl = (ltp - pos["entry"]) * pos["qty"]

            if pos["side"] == "SELL":
                pnl = -pnl

            pos["pnl"] = pnl

    def close_position(self, pos, exit_price):

        pnl = (exit_price - pos["entry"]) * pos["qty"]

        if pos["side"] == "SELL":
            pnl = -pnl

        self.pnl += pnl
        pos["open"] = False

        print(f"[PAPER EXIT] {pos['symbol']} PnL: {pnl}")
