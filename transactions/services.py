
def classify_transaction(transaction_type):
    non_financial = ['Balance Checked', 'Mini Statement','Balance Inquiry','Transaction Failed','Pin Change']
    if transaction_type in non_financial:
        return "Non-Financial"
    
    return "Financial"
        