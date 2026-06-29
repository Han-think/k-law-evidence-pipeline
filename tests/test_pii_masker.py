from klep.security.pii_masker import mask_sensitive_text


def test_mask_email():
    assert "[EMAIL]" in mask_sensitive_text("contact test@example.com")


def test_mask_phone():
    assert "[PHONE]" in mask_sensitive_text("phone 010-1234-5678")
