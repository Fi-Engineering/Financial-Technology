def print_receipt(subtotal, tax_rate, tip_rate):
    """Displays each component of a restaurant bill, 
       including subtotal, tax and tip, and the total amount due, formatted as per example."""
    
    print('Subtotal: $%10.2f'%(subtotal))
    print('     Tax: $%10.2f'%(subtotal*tax_rate))
    print('     Tip: $%10.2f'%(subtotal*tip_rate))
    print('           ==========')
    total = subtotal + subtotal*tax_rate + subtotal*tip_rate
    print('   Total: $%10.2f'%( total), '\n')

