import pandas as pd
from fpdf import FPDF

# Read CSV file
data = pd.read_csv("student_marks.csv")

# Analyze data
total_students = len(data)
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Student Marks Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(200, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(200, 10, f"Lowest Marks: {lowest_marks}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Student Data:", ln=True)

for index, row in data.iterrows():
    pdf.cell(200, 8, f"{row['Student Name']} - {row['Marks']}", ln=True)

# Save PDF
pdf.output("student_report.pdf")

print("Student Report Generated Successfully!")
    
