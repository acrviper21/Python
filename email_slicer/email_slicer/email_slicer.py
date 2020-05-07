# By: Erik Sistos
# Date 20200506
# Description: This program ask for an email address and outputs the user and domain 

# get user email address
email = input("What is your email address?: ").strip()

# slice out user name
user_name = email[:email.index("@")]

# slice domain name
domain_name = email[email.index("@")+1:]

# format message
output = "Your username is {} and your domain name is {}".format(user_name, domain_name)

# display output message
print(output)