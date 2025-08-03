import pandas as pd
df = pd.read_csv(r"C:\Users\Aadarsh\Desktop\Book1.csv")


df['fiscal year'] = df['fiscal year'].astype(int)

df = df.sort_values(by=['company', 'fiscal year'])

df['revenue growth (%)'] = df.groupby('company')['total revenue'].pct_change() * 100
df['net income growth (%)'] = df.groupby('company')['net income'].pct_change() * 100
df['assets growth (%)'] = df.groupby('company')['total assets'].pct_change() * 100
df['liabilities growth (%)'] = df.groupby('company')['total liabilities'].pct_change() * 100
df['cash flow growth (%)'] = df.groupby('company')['operating cash flow'].pct_change() * 100

print("\nData with growth percentages:")
print(df)
