import re
import random
import string

def check_email_format(email):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Nevalidní formát emailu")
    return "Email je v pořádku"

def generate_valid_email():
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.org']
    username = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(5,12)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_invalid_email():
    invalid_formats = [
        "missing_at_symbol.com",  # Chybějící zavináč
        "@missing_username.com",  # Chybějící uživatelské jméno
        "invalid_domain@com",  # Neplatná doména
        "no_tld@domain.",  # Chybějící TLD
        "spaces in@address.com",  # Mezery v adrese
        "special!chars@email.com",  # Neplatné znaky
    ]
    return random.choice(invalid_formats)

def email_generator(count = 10, valid_ratio =0.5):
    valid_count = int(count * valid_ratio)
    invalid_count = count - valid_count
    emails = [generate_valid_email() for _ in range(valid_count)] + [generate_invalid_email() for _ in range(invalid_count)]
    random.shuffle(emails)
    return emails


if __name__ == '__main__':
    print(check_email_format("richardegydy@gmail.com"))
