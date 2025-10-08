print("Hola copilot HI")
varnum = 5
varstr = "Gercogcb"
print(varnum)
print(varstr)
n=5
def calculate_fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
print(calculate_fibonacci(n))
# Funcion que analiza una lista de emails y valida si son corrctos
email_list = ["germancb79@gmail.com", "invalid-email", "test@example.com"]
def validate_emails(email_list):
    import re
    valid_emails = []
    invalid_emails = []
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    for email in email_list:
        if email_pattern.match(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    
    return valid_emails, invalid_emails
# Funcion para imprimir emails validos y no validos
valid_emails, invalid_emails = validate_emails(email_list)
print("Emails válidos:")
for email in valid_emails:
    print(email)
print("Emails no válidos:")
for email in invalid_emails:
    print(email)
