from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet # type: ignore
import openpyxl


PASTA_RAIZ = Path(__file__).parent
WORKBOOK_PATH = PASTA_RAIZ / 'workbook.xlsx'

workbook = openpyxl.Workbook()
sheet = 

students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]