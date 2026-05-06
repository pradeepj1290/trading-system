class Regime:

    def detect(self, df):

        atr = df["high"].rolling(14).max() - df["low"].rolling(14).min()
        price = df["close"]

        trend_strength = abs(price.iloc[-1] - price.iloc[-20]) / atr.iloc[-1]

        if trend_strength > 1.5:
            return "TREND"

        return "RANGE"
