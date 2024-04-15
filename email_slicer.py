def main():
    print("email slicer")
    email=input("Input your email address: ")
    (username,domain)=email.split("@")
    (domain,extension)=domain.split(".")
    print("Username : ",username)
    print("domain :", domain)
    print("Extension : ",extension)
main()

