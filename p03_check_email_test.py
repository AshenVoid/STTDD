import pytest
from p03_check_email import *

@pytest.fixture()
def provide_email():
    print("\nPříprava email účtu")
    emails = email_generator(100, 0.5)
    yield emails
    print("\nÚklid po testování")

def test_email_exception(provide_email):
    valid_count = 0
    invalid_count = 0
    raised_exceptions = 0

    for email in provide_email:
        try:
            with pytest.raises(Exception):
                check_email_format(email)
                print(f"✅ {email} - Validní formát")
                valid_count += 1
        except pytest.raises.Exception:
            print(f"❌ {email} - Nevalidní formát")
            invalid_count += 1
            raised_exceptions += 1
    print(
        f"\nShrnutí testu: {valid_count} validních e-mailů, {invalid_count} "
        f"nevalidních e-mailů, {raised_exceptions} vyvolaných výjimek.")
    assert raised_exceptions == invalid_count