import pandas as pd

data = {
    "Set A": [85, 90, 95, 100, 105],
    "Set B": [70, 80, 95, 110, 120]
    }

df = pd.DataFrame(data)

std_A = df["Set A"].std()
std_B = df["Set B"].std()

print(f"Стандартное отклонение для Set A: {std_A}")
print(f"Стандартное отклонение для Set B: {std_B}")
