import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

print("\nDataFrame setelah peningkatan gaji 5%:")
print(df)

print("\nRingkasan perubahan setelah peningkatan gaji 5%:")
for index, row in df.iterrows():
    print(f"{row['Nama']} - Gaji Baru: {row['Gaji']:.2f}")

df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)


print("\nDataFrame setelah peningkatan tambahan 2% untuk usia > 30:")
print(df)

print("\nRingkasan perubahan setelah peningkatan tambahan:")
for index, row in df.iterrows():
    if row['Usia'] > 30:
        print(f"{row['Nama']} - Usia: {row['Usia']}, Gaji Baru: {row['Gaji']:.2f}")
