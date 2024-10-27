# hisabkitab
A simple CLI tool to keep track of your dues 

# List all hisab  
hisabkitab hisab

# Lists all entries with status 'to_pay' 
hisabkitab add taseng 1000

# Lists all entries with status 'to_pay' 
hisabkitab list to_pay

# Update hisab of taseng 
hisabkitab update taseng --amount 100

# Update hisab if paid 90 to taseng
python3 hisabkitab.py update taseng --paid 90

