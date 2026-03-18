import os
import re
import json
from fpdf import FPDF
from datetime import datetime

def sanitize_text(text):
    """Remove characters that FPDF doesn't support in standard fonts and strip JSON/XML artifacts."""
    if not text:
        return ""
    
    text = re.sub(r'\{"type":\s*"function".*?\}', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<function=.*?>.*?</function>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'\{"content":.*?"topic":.*?\}', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    json_pattern = r'\{[\s\n]*"content"[\s\n]*:[\s\n]*".*?"[\s\n]*(,[\s\n]*".*?"[\s\n]*:[\s\n]*".*?"[\s\n]*)*\}'
    text = re.sub(json_pattern, '', text, flags=re.DOTALL)
    
    text = text.replace('\u2013', '-').replace('\u2014', '-').replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    
    try:
        return text.encode('latin-1', 'ignore').decode('latin-1')
    except:
        return text.encode('ascii', 'ignore').decode('ascii')

def strip_markdown(text):
    """Strip markdown bold/italic markers from text for clean PDF output."""
    if not text:
        return ""
    return re.sub(r'[\*_]{1,2}(.*?)[\*_]{1,2}', r'\1', text)

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150)
            self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d")}', ln=True, align='R')
            self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(180)
        self.cell(0, 10, f'Page {self.page_no()} | Swarm Intelligence Blog', align='C')

def generate_pdf(markdown_content, output_path, title="Blog Post"):
    """
    Converts markdown content to a formatted PDF with professional layout.
    """
    try:
        markdown_content = markdown_content.strip()
        
        if markdown_content.startswith('{') and '"content"' in markdown_content:
            try:
                data = json.loads(markdown_content)
                markdown_content = data.get('content', markdown_content)
                if not title or title == "Blog Post":
                    title = data.get('title', title)
            except:
                pass

        pdf = PDF()
        pdf.set_margins(25, 30, 25)
        pdf.add_page()
        effective_width = pdf.w - pdf.l_margin - pdf.r_margin
        
        pdf.set_font("Helvetica", "B", 26)
        pdf.set_text_color(20, 20, 20)
        pdf.multi_cell(effective_width, 18, strip_markdown(sanitize_text(title)), align='C')
        pdf.set_draw_color(100, 100, 100)
        pdf.line(pdf.l_margin, pdf.get_y() + 5, pdf.w - pdf.r_margin, pdf.get_y() + 5)
        pdf.ln(15)
        
        lines = markdown_content.split('\n')
        for line in lines:
            text = line.strip()
            if not text:
                pdf.ln(4)
                continue
            
            clean_text = sanitize_text(text)
            if not clean_text: continue

            pdf.set_x(pdf.l_margin)

            if text.startswith('###'):
                pdf.set_font("Helvetica", "B", 13)
                pdf.set_text_color(60, 60, 60)
                pdf.multi_cell(effective_width, 9, strip_markdown(clean_text).replace('###', '').strip())
                pdf.ln(2)
            elif text.startswith('##'):
                pdf.ln(5)
                pdf.set_font("Helvetica", "B", 16)
                pdf.set_text_color(40, 40, 40)
                pdf.multi_cell(effective_width, 11, strip_markdown(clean_text).replace('##', '').strip())
                pdf.ln(3)
            elif text.startswith('#'):
                pdf.ln(5)
                pdf.set_font("Helvetica", "B", 20)
                pdf.set_text_color(20, 20, 20)
                pdf.multi_cell(effective_width, 14, strip_markdown(clean_text).replace('#', '').strip())
                pdf.ln(4)
            elif re.match(r'^(\d+\.|\-|\*)\s', text):
                pdf.set_font("Helvetica", "", 11)
                pdf.set_text_color(40, 40, 40)
                pdf.set_x(pdf.l_margin + 5)
                prefix = "o " if text.startswith(('-', '*')) else ""
                content = text if not prefix else prefix + text[2:]
                pdf.multi_cell(effective_width - 5, 8, strip_markdown(sanitize_text(content)))
            else:
                pdf.set_font("Helvetica", "", 11)
                pdf.set_text_color(30, 30, 30)
                pdf.multi_cell(effective_width, 7, strip_markdown(clean_text))
        
        pdf.output(output_path)
        return True
    except Exception as e:
        print(f"Error in PDF generation: {e}")
        return False

if __name__ == "__main__":
    generate_pdf("# Test Title\nThis is a *test* content.", "test.pdf", "My Test Title")
