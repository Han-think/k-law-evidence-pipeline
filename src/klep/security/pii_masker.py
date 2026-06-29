"""Simple local masking utilities.

This module is intentionally conservative and dependency-light.
It is not perfect. It is a first safety layer before optional external API use.
"""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?82[- ]?)?0?1[016789][- ]?\d{3,4}[- ]?\d{4}(?!\d)")
LONG_NUMBER_RE = re.compile(r"(?<!\d)\d{6,}(?!\d)")


def mask_sensitive_text(text: str) -> str:
    """Mask common private patterns in Korean case notes.

    This is only a helper. Users should still review outgoing text manually.
    """
    masked = EMAIL_RE.sub("[EMAIL]", text)
    masked = PHONE_RE.sub("[PHONE]", masked)
    masked = LONG_NUMBER_RE.sub("[NUMBER]", masked)
    return masked
