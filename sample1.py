invoice_no=7
customer='john doe'
amount=199.99
txt=''
print(txt.center(30,'='))
print('INVOICE'.center(30))
print(f'Invoice No: INV-{str(invoice_no).rjust(5,'0')}'.center(30))
print(f'Customer: {customer.title()}'.center(30))
print(f'Amount: {amount}'.center(30))
print(txt.center(30,'='))