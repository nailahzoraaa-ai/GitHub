import json
import pandas as pd

# Baca file JSON
with open("Na'ila Zora Agustin_V3925049.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Buat writer untuk Excel
with pd.ExcelWriter("output_data.xlsx", engine="openpyxl") as writer:
    # Loop tiap bagian data di JSON
    for key, value in data.items():
        # Konversi list of dict ke DataFrame
        df = pd.DataFrame(value)
        # Tulis ke sheet dengan nama key
        df.to_excel(writer, sheet_name=key, index=False)

print("Berhasil mengubah JSON ke Excel: output_data.xlsx")
