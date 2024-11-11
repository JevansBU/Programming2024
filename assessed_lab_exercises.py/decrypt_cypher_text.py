def decrypt_cypher_text(encrypted_text, key):

    # function implementation here...

    decrypted_text = ""
    for character in encrypted_text:
        decrypt_letter = (ord(character) - key) % 256
        decrypt_letter = chr(decrypt_letter)
        decrypted_text += decrypt_letter
    
    return decrypted_text

result = decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3)
print(result)

#Each error you make in programming is an opportunity to become a better developer!