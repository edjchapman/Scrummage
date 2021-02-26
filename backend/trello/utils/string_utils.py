import re


def get_est(text: str) -> str:
    """
    Extract estimate from text by matching numbers between brackets.
    """
    est = None
    try:
        match = re.findall('\(*[.0-9 ]+\)', text)
        if match:
            est = match[0]
            est = est.strip("( )")
            est = float(est)
    except Exception:
        est = None
    return est
