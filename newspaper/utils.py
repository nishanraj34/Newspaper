
def rabin_karp_search(text, pattern):
    if not text or not pattern:
        return False
    
    if len(pattern) > len(text):
        return False

    d = 256  # number of characters in the input alphabet
    q = 101  # a prime number
    M = len(pattern)
    N = len(text)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h * d) % q

    # Calculate hash value for pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and pattern
        if p == t:
            # Check for characters one by one
            if text[i:i+M] == pattern:
                return True  # Pattern found

        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < N-M:
            t = (d*(t - ord(text[i])*h) + ord(text[i+M])) % q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t + q

    return False  # Pattern not found

def search_in_post_title(post, keyword):
    """Search for a keyword in post title using Rabin-Karp"""
    return rabin_karp_search(post.title.lower(), keyword.lower())






