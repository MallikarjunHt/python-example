def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        x=list(word)
        if x[0].isupper():
            result +=x[0]
        elif x[0].islower():
            result +=x[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS