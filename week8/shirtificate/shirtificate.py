from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 15, 80, 180)
        self.set_font("helvetica", "B", 50)
        self.cell(190, 65, "CS50 Shirtificate", align="c")

    def footer(self):
        self.set_y(-10)
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(190, -265, f"{name} took CS50", align="c")


name = input("name: ")
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
