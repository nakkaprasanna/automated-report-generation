import pandas as pd
from fpdf import FPDF

# Read data
df = pd.read_csv("sample_data.csv")

# Simple analysis
summary = df.describe()

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Data Report", ln=True, align='C')

for col in summary.columns:
    pdf.cell(200, 10, txt=f"{col} Summary:", ln=True)
    for idx in summary.index:
        val = summary.loc[idx, col]
        pdf.cell(200, 10, txt=f"{idx}: {val:.2f}", ln=True)

pdf.output("report.pdf")
