import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Read CSV file
data = pd.read_csv("student_marks.csv")

# Perform Analysis
total_marks = data["Marks"].sum()
number_of_subjects = len(data)
percentage = total_marks / number_of_subjects

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

# Create PDF
doc = SimpleDocTemplate("Student_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("AUTOMATED STUDENT REPORT", styles["Title"]))
elements.append(Spacer(1, 20))

# Add table
table_data = [["Subject", "Marks"]]
for i in range(len(data)):
    table_data.append([data["Subject"][i], data["Marks"][i]])

table = Table(table_data)
elements.append(table)

elements.append(Spacer(1, 20))
elements.append(Paragraph(f"Total Marks: {total_marks}", styles["Heading2"]))
elements.append(Paragraph(f"Percentage: {round(percentage,2)}%", styles["Heading2"]))
elements.append(Paragraph(f"Grade: {grade}", styles["Heading2"]))

doc.build(elements)

print("Report Generated Successfully!")
