''' Hiram Rios 80552404 teusday 10:30
the purpose of this lab is to practice avl trees and btress using embeddings
and manipulate them in different methods

'''
from RbtNode import RBTNode
from redtree import RedBlackTree
from AvlTree import AVLTree
from AvlNode import AVL_Node
import math


# the dot porduct willl be used to find the similarity pair of words

def dot(x, y):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (float(x.embeddings[i]) * float(y.embeddings[i]))
    return sum


# this method will find the magnitude of the word  within the embedding
def Magnitude(n):
    sum = 0
    for i in range(len(n.embeddings)):
        sum += (math.pow(float(n.embeddings[i]), 2))
    return math.sqrt(sum)


# this method will find the similarity between the pair of wordds
def similar(x, y):
    if x is None:
        print('x')
    if y is None:
        print('y')
    mg1 = Magnitude(x)
    mg2 = Magnitude(y)
    dotPro = dot(x, y)
    similar = (dotPro) / (mg1 * mg2)
    return similar


# this method computes the number of nodes in a tree
def countNodes(n):
    if n == None:
        return 0
    return 1 + countNodes(n.left) + countNodes(n.right)


# this method the number height in atree
def height(n):
    if n != None:
        left = height(n.left)
        right = height(n.right)
        if left > right:
            return 1 + left
        return 1 + right
    return -1





# this method count the number of nodes in a btree
def count_BtreeNodes(T):
    count = 1
    if T.isLeaf:
        return 1
    for i in range(T.n):
        count += count_BtreeNodes(T.c[i])
    return count


# this method is for the height of a btree
def height_Btree(T):
    if T == None:
        return -1
    if T.isLeaf:
        return 0
    return 1 + height_Btree(T.c[0])




#text = "/users/hiramrios/PycharmProjects/Lab3/glove.6B.40d.txt"

while True:
    choice = raw_input("which tree woul you prefer? AVL, a or Red-Black Tree, r")
    if choice == 'a' or choice == 'r':
        break
    print('Invalid choice')
if choice == 'a':
    tree = AVLTree()
elif choice == 'r':
    tree = RedBlackTree()

with open("glove.6B.50d.txt") as f:
    for line in f:
        info = line.split(' ')
        if info[0][0].isalpha():
            if choice is 'a':
                node = AVL_Node(info[0], info[1:])
                tree.insert(node)
            elif choice is 'r':
                tree.insert(info[0], info[1:])




with open( "smiliraities.txt") as textFiles:
    for line in textFiles:
        words = line.split(' ')
        firstWord = words[0]
        secondWord = words[1].rstrip('\n')
        node1 = tree.search(firstWord)
        node2 = tree.search(secondWord)
        if node1 and node2:
            print(firstWord + ' ' + secondWord + ' ' + str(similar(node1, node2)))
temp = tree.root





