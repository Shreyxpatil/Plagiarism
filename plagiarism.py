from difflib import SequenceMatcher

with open("1.txt") as file1 , open("2.txt") as file2:
    fil1data=file1.read()
    file2data=file2.read()
    sim=SequenceMatcher(None,fil1data,file2data).ratio()
    print("Similarity:",sim*100)