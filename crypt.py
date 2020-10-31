class Code():
    def __init__(self, number = 3):
        self.number = number
    

    def code(self ,message: str):
        new_message = ''
        for letter in message:
            if letter.isalpha():
                new_letter = ord(letter) + self.number
                if letter.isupper():
                    if new_letter > 90:
                        new_letter -= 26
                    elif new_letter < 65:
                        new_letter += 26 
                else:
                    if new_letter > 122:
                        new_letter -= 26
                    elif new_letter < 97:
                        new_letter += 26
                new_message += chr(new_letter)
            else:
                new_message += letter
        return new_message

    def decode(self, crypted_message):
        encrypted_message = ''
        for letter in crypted_message:
            if letter.isalpha():
                new_letter = ord(letter) - self.number
                if letter.isupper():
                    if new_letter > 90:
                        new_letter -= 26
                    elif new_letter < 65:
                        new_letter += 26 
                else:
                    if new_letter > 122:
                        new_letter -= 26
                    elif new_letter < 97:
                        new_letter += 26
                encrypted_message += chr(new_letter)
            else:
                encrypted_message += letter
        return encrypted_message


        