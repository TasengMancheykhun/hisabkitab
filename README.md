# hisabkitab
A simple CLI tool to keep track of your dues 

Run the project

1. List all hisab  
   ```hisabkitab hisab```

Say 'Ramesh' is a person,

2. Add an entry to pay 1000 to Ramesh
   ```hisabkitab add ramesh 1000```

3. Lists all entries with status 'to_pay' 
   ```hisabkitab list to_pay```

4. Update hisab of Ramesh 
   ```hisabkitab update ramesh --amount 100```

5. Update hisab if paid 90 to Ramesh
   ```python3 hisabkitab.py update ramesh --paid 90```

