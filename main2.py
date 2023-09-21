from bintreeFile import Bintree
from LinkedQFile import LinkedQ


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

    def writechain(self):
        if self.parent != None:
            self.parent.writechain()
            print(self.word)
        else:
            print(self.word)


def makechildren(startNode, q, slutord, svenska, gamla):
    found = False
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
    for i in range(0, 3):
        barn = [*startNode.word]
        for searchletter in letters:
            barn[i] = searchletter
            newword = barn[0]+barn[1]+barn[2]
            if newword in svenska and not newword in gamla and newword != startNode.word:
                if newword == slutord:
                    found = True
                    newNode = ParentNode(newword)
                    newNode.parent = startNode
                    print('Vägen är denna:')
                    newNode.writechain()

                newNode = ParentNode(newword)
                newNode.parent = startNode
                q.enqueue(newNode)
                gamla.put(newword)
    return found


def main():
    svenska = Bintree()
    gamla = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                None
            else:
                svenska.put(ordet)
 # --------------------------------------------------------

    q = LinkedQ()
    startord = input('Skriv in startord:')
    slutord = input('Skriv in slutord:')
    startNode = ParentNode(startord)
    q.enqueue(startNode)

 # -------------------------------------------------------

    found = False
    while not found and not q.isEmpty():
        wordNode = q.dequeue()
        found = makechildren(wordNode, q, slutord, svenska, gamla)
        if found:
            break
    if not found:
        print("Det finns ingen väg till", slutord)


main()
