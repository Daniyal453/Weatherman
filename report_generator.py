from fpdf import FPDF
import os

from constants import PdfMessages


class PdfMaker:
    """
    Generates PDF For Result
    """
    def __init__(self, output, file_name) -> None:
        self.output = output
        self.file_name = file_name
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font(PdfMessages.FONT_ARIAL, size=16)

    def pdf_maker(self,description):
        """
        Takes output result,
        Generates Pdf
        """
        for key, value in zip(description, self.output):
            self.pdf.cell(100, 10, txt=key, align="C")
            self.pdf.cell(40, 10, txt="-------", align="C")
            self.pdf.cell(30, 10, txt=value, align="C", ln=1)
        
        self.save_pdf()

    def bar_pdf_maker(self):
        """
        Takes month horizontal bar temp list,
        Generates Pdf
        """
        for value in self.output:
            exclude_last_char = value[:-1]
            splt_output = exclude_last_char.split(' ')

            self.pdf.set_text_color(0, 0, 0)
            self.pdf.cell(70, 10, txt=splt_output[0], align="C")

            if PdfMessages.RED_FLAG in value:
                self.pdf.set_text_color(255, 0, 0)
                self.pdf.cell(60, 10, txt=splt_output[1], align="C")
            elif PdfMessages.BLUE_FLAG in value:
                self.pdf.set_text_color(0, 0, 255)
                self.pdf.cell(60, 10, txt=splt_output[1], align="C")

            self.pdf.set_text_color(0, 0, 0)
            self.pdf.cell(70, 10, txt=splt_output[2], align="C", ln=1)

        self.save_pdf()
    
    def save_pdf(self):
        """
        Saves pdf to specified location
        """
        if not os.path.isdir(PdfMessages.PATH_TO_SAVE_PDF):
            os.mkdir(PdfMessages.PATH_TO_SAVE_PDF)

        self.pdf.output(
            PdfMessages.PDF_OUTPUT.format(
                path_to_save=PdfMessages.PATH_TO_SAVE_PDF,
                file_name=self.file_name)
        )

