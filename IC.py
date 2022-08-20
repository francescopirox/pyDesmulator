class Ic:
    mean_value: float
    quantile: float

    def __init__(self, mean_value, quantile) -> None:
        self.quantile = quantile
        self.mean_value = mean_value

    #Deafault 95
    def __str__(self) -> str:
        return (self.mean_value-(1.65*self.quantile)).__str__()+" <-> "+ (self.mean_value+(1.65*self.quantile)).__str__()

