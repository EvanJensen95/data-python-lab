open_file = open("CupcakeInvoices.csv")

# for row in open_file:
#   print(row)


# for row in open_file:
#   values = row.split(',')
#   print(values[2])

# for row in open_file:
#     values = row.split(',')
#     total_invoice = int(values[3]) * float(values[4])
#     print(total_invoice)


total_invoices = 0

for row in open_file:
  values = row.split(',')
  total_invoices = total_invoices + (int(values[3]) * float(values[4]))

print(total_invoices)


open_file.close()