# Assign 'import_file' to the name of the file and 'remove_list' to the "block list"
import_file: str = "allow_list.txt"
remove_list: list[str] = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Use 'with' to read the file and store the content into 'ip_addresses'
with open(import_file, "r") as file:
  ip_addresses: str = file.read()

# Convert 'ip_addresses' to a list
ip_addresses = ip_addresses.split()

# Loop through 'ip_addresses' and remove elements present into 'remove_list'
for element in ip_addresses:
  if element in remove_list:
    ip_addresses.remove(element)

# Convert 'ip_addresses' back to a string so that it can be written into the text file
ip_addresses = "\n".join(ip_addresses)

# Use 'with' to rewrite the original file
with open(import_file, "w") as file:
  file.write(ip_addresses)

# Use 'with' to read in the updated file
with open(import_file, 'r') as file:
  # Read in the updated file and store the contents in 'text'
  text: str = file.read()

# Display the contents of 'text'
print(text)
