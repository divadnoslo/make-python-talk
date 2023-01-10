from mysr import voice_to_text

# Begin Infinite Loop
while True:
    inp = ""

    # Begin to Listen:
    inp = voice_to_text()
    
    # Print what I said
    print(f"You just said: {inp}")
    
    # Break From Loop
    if inp == "stop listening":
        print("Bye!")
        break