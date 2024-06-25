{"changed":true,"filter":false,"title":"caesar_debug-3.py","tooltip":"/caesar_debug-3.py","value":"# Module Lab: Caesar Cipher Program Bug #3\n#\n# In a previous lab, you created a Caesar cipher program. This version of\n# the program is buggy. Use a debugger to find the bug and fix it.\n\n# Double the given alphabet\ndef getDoubleAlphabet(alphabet):\n    doubleAlphabet = alphabet + alphabet\n    return doubleAlphabet\n\n# Get a message to encrypt\ndef getMessage():\n    stringToEncrypt = input(\"Please enter a message to encrypt: \")\n    return stringToEncrypt\n\n# Get a cipher key\ndef getCipherKey():\n    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")\n    return shiftAmount\n\n# Encrypt message\ndef encryptMessage(message, cipherKey, alphabet):\n    encryptedMessage = \"\"\n    uppercaseMessage = \"\"\n    uppercaseMessage = message.upper()\n    for currentCharacter in uppercaseMessage:\n        position = alphabet.find(currentCharacter)\n        newPosition = position + int(cipherKey)\n        if currentCharacter in alphabet:\n            encryptedMessage = encryptedMessage + alphabet[newPosition]\n        else:\n            encryptedMessage = encryptedMessage + currentCharacter\n    return encryptedMessage\n\n# Decrypt message\ndef decryptMessage(message, cipherKey, alphabet):\n    decryptKey = -1 * int(cipherKey)\n    return encryptMessage(message, decryptKey, alphabet)\n\n# Main program logic\ndef runCaesarCipherProgram():\n    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n    print(f'Alphabet: {myAlphabet}')\n    myAlphabet2 = getDoubleAlphabet(myAlphabet)\n    print(f'Alphabet2: {myAlphabet2}')\n    myMessage = getMessage()\n    print(myMessage)\n    myCipherKey = getCipherKey()\n    print(myCipherKey)\n    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)\n    print(f'Encrypted Message: {myEncryptedMessage}')\n    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)\n    print(f'Decrypted Message: {myDecryptedMessage}')\n\n# Main logic\nrunCaesarCipherProgram()","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":11}],[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":12}],[{"start":{"row":37,"column":43},"end":{"row":37,"column":44},"action":"remove","lines":["y"],"id":13},{"start":{"row":37,"column":42},"end":{"row":37,"column":43},"action":"remove","lines":["e"]},{"start":{"row":37,"column":41},"end":{"row":37,"column":42},"action":"remove","lines":["K"]},{"start":{"row":37,"column":40},"end":{"row":37,"column":41},"action":"remove","lines":["r"]},{"start":{"row":37,"column":39},"end":{"row":37,"column":40},"action":"remove","lines":["e"]},{"start":{"row":37,"column":38},"end":{"row":37,"column":39},"action":"remove","lines":["h"]},{"start":{"row":37,"column":37},"end":{"row":37,"column":38},"action":"remove","lines":["p"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"remove","lines":["i"]},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"remove","lines":["c"]}],[{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["d"],"id":14},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["e"]},{"start":{"row":37,"column":37},"end":{"row":37,"column":38},"action":"insert","lines":["c"]},{"start":{"row":37,"column":38},"end":{"row":37,"column":39},"action":"insert","lines":["r"]}],[{"start":{"row":37,"column":39},"end":{"row":37,"column":40},"action":"insert","lines":["y"],"id":15}],[{"start":{"row":37,"column":35},"end":{"row":37,"column":40},"action":"remove","lines":["decry"],"id":16},{"start":{"row":37,"column":35},"end":{"row":37,"column":45},"action":"insert","lines":["decryptKey"]}],[{"start":{"row":12,"column":66},"end":{"row":12,"column":70},"action":"remove","lines":["    "],"id":17},{"start":{"row":12,"column":66},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":66},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":18}]]},"ace":{"folds":[],"scrolltop":315.83332626907895,"scrollleft":0,"selection":{"start":{"row":12,"column":66},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1719305644025}