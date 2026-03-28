import pandas as pd

data = pd.read_csv("binding_energy_results.csv")

data["Running_Average"] = data["DeltaG_bind"].expanding().mean()

data.to_csv("convergence_data.csv", index=False)

print("MM/GBSA convergence analysis complete.")
