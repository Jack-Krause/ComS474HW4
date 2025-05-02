import os
import re
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
print(f"Current directory: {cwd}")

log_files = glob.glob(os.path.join(cwd, "*.log"))
if not log_files:
    raise FileNotFoundError("log files not found.")

write_dir = os.path.join(cwd, 'parsedcleancsv')
os.makedirs(write_dir, exist_ok=True)

re_pattern = r"\d{1,2}\.\d{1,3}\%"

dtypes = np.dtype([('epoch', int), ('percentage', float)])

for f in log_files:
    epoch = 0
    data = []

    with open(f, 'r') as open_file:
        for line in open_file:
            match = re.search(re_pattern, line)

            if match:
                val = match.group(0).replace('%', '')
                data.append((epoch, float(val)))
                epoch += 1
            else:
                print(f"WARNING: no match found. Line is:\n`{line}`(end of line)")

    if data:
        np_array = np.array(data, dtype=dtypes)
        df = pd.DataFrame(np_array)
    else:
        df = pd.DataFrame(columns=['epoch', 'percentage'])

    basename = os.path.basename(f)
    outpath = os.path.join(write_dir, basename.replace('.log', '.csv'))
    df.to_csv(outpath, index=False)
    
    
csv_files = [f for f in os.listdir(write_dir) if f.endswith('.csv')]

for csv_f in csv_files:
    """
    Do some data analysis & calculation for each model
    """
    path = os.path.join(write_dir, csv_f)
    df = pd.read_csv(path)
    model_name = csv_f.replace('.csv', '')
    print(f"\n\n---{model_name}---")
    
    # find the area under the curve
    area = np.trapezoid(df['percentage'], df['epoch'])
    print(f"Area = {area}")
    # find peak percentage for this model
    max_accuracy = df['percentage'].max()
    print(f"Max %: {max_accuracy}")
    # find end accuracy
    end_accuracy = df['percentage'].iloc[-1]
    print(f"End %: {end_accuracy}")
    # find num of epochs needed to reach 80%
    epoch_threshold_reached = (df['percentage'] > 80).idxmax()
    print(f"Epoch reached 80%: {epoch_threshold_reached}")
    
    
    # plt.plot(df['epoch'], df['percentage'], label=csv_f.replace('.csv', ''))
    # plt.show()



