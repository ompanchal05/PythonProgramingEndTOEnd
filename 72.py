#Introduction of the Panda 

import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Om', 'Raj', 'Asha', 'Neha'],
    'Age': [21, 22, 23, 20],
    'City': ['Mumbai', 'Pune', 'Delhi', 'Surat']
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
