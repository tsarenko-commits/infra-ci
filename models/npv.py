import numpy as np

def npv(cashflows, rate=0.12):
    return sum(cf / (1 + rate)**i for i, cf in enumerate(cashflows, 1))

if __name__ == "__main__":
    scenarios = {
        "base": [-500, 120, 130, 140, 150, 160],
        "high": [-500, 150, 170, 190, 210, 230],
    }
    for name, cf in scenarios.items():
        print(f"{name}: NPV = {npv(cf, 0.12):.1f} млн ₽")
