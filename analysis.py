import os
import re
import glob


cwd = os.getcwd()
print(cwd)

log_files = glob.glob(os.path.join(cwd, "*.log"))
if not log_files:
    raise FileNotFoundError("log files not found.")

write_dir = os.path.join(cwd, 'parsedclean')
if not os.path.exists(write_dir):
    os.mkdir(write_dir)

re_pattern = r"\d{1,2}\.\d{1,3}\%"

for f in log_files:
    print(f)
    contents_str = ""
    with open(f, 'r') as open_file:
        for line in open_file:
            match = re.search(re_pattern, line)
            print(f"match:\n{match}")
            
            if match:
                contents_str += match.group(0).replace('%', '') + "\n"
                
    basename = os.path.basename(f)
    with open(os.path.join(write_dir, basename), 'w') as write_file:
        write_file.write(contents_str)




