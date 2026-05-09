from fpdf import FPDF
import os

class EcosystemReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Data Science Ecosystem: Consumer Behavior Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_report():
    pdf = EcosystemReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    # 1. الرؤية الإنسانية
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Human-Centric Data Vision", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, (
        "This project explores the intersection of data engineering and psychological capital. "
        "By analyzing user journeys, we aim to build digital environments that are not only "
        "efficient but also humanized."
    ))
    pdf.ln(5)

    # 2. المنهجية التقنية
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Ecosystem Methodology", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, (
        "A synthetic big data environment was simulated featuring 500 unique user sessions. "
        "Key metrics include device segmentation, session depth, and conversion probability models."
    ))
    pdf.ln(5)

    # 3. التحليل المرئي - الرسم الأول
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. Behavioral Insights", 0, 1)
    
    if os.path.exists('figures/device_conversion.png'):
        pdf.image('figures/device_conversion.png', x=15, w=170)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Figure 1: Comparison of conversion rates between Mobile, Desktop, and Tablet users.", 0, 1, 'C')

    pdf.add_page()
    
    # 3. التحليل المرئي - الرسم الثاني
    if os.path.exists('figures/behavior_scatter.png'):
        pdf.image('figures/behavior_scatter.png', x=15, w=170)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Figure 2: Correlation between session duration and pages visited.", 0, 1, 'C')

    # 4. التوصيات الاستراتيجية
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "4. Strategic Recommendations", 0, 1)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, (
        "1. Optimize Mobile UX to bridge the conversion gap between devices.\n"
        "2. Focus on psychological engagement points to extend session duration.\n"
        "3. Implement predictive models to humanize digital workplace environments."
    ))

    output_path = 'outputs/Data_Science_Ecosystem_Report.pdf'
    pdf.output(output_path)
    print(f"Ecosystem PDF report generated at: {output_path}")

if __name__ == "__main__":
    create_pdf_report()