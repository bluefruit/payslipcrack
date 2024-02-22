from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import WrongPasswordError
from datetime import datetime, timedelta
import sys

if len(sys.argv) != 2:
	print(f'Usage: {sys.argv[0]} <initials>')
	exit(1)

initials = sys.argv[1].upper()

birthday = datetime(1960, 1, 1)
stop = datetime(2010, 1, 1)
delta = timedelta(days=1)

while birthday < stop:
	if birthday.month == 1 and birthday.day == 1:
		print(f'Year: {birthday.year}')

	password = f'{initials}{birthday.strftime("%d%m%Y")}'

	try:
		reader = PdfReader("PaySlip.pdf", password=password)

		with PdfWriter("nopassword.pdf") as writer:
			for page in reader.pages:
				writer.add_page(page)

		print(f'password was: {password}')

		exit(0)
	except WrongPasswordError:
		pass

	birthday = birthday + delta
