'''
Optimal Solution: As per the question we know we can form an email by adding local_name + "@" + domain_name.
Anything after "+" is ignored and anything after "." is just added to local_name. We have to find the unique emails
As we know hashset stores unique items only. So we will use hashset. First we will split the given emails in local_name and domain_name
After that we will replace "." with ""(empty space). We will split the local_name if we find any "+"
finally we will reconstruct the email with define form. After that we will add those email to set.
Finally we will print the len of set.
'''


def leetcode929(emails):
    unique_emails: set[str] = set()
    for email in emails:
        local_name, domain_name = email.split("@")
        local_name = local_name.split('+')[0]
        local_name = local_name.replace(".", "")
        email = local_name + "@" + domain_name
        unique_emails.add(email)
    print(len(unique_emails))


def main():
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bb.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    leetcode929(emails)


if __name__ == "__main__":
    main()
