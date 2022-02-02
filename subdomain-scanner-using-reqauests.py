# opening the subdomain text file in the read mode
with open('subdomain_names.txt','r') as file:
   
    # reading the file
    name = file.read()
     
    # using spilitlines() function storing the list
    # of spitted strings
    sub_dom = name.splitlines()
     
    # printing number of subdomain names present in
    # the list
    print(f"Number of subdomain names present in the file are: {len(sub_dom)}\n")
     
    # printing list of subdomain names present in the
    # text file
    print("List of subdomain names present in the file\n")
    print(sub_dom)