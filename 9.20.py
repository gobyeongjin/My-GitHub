if __name__ == "__main__":
    node=[0,1,2,3,4,5,6,7,8,9]

    root =None
    for i in node:
        n= BSTNode(i)
        if root == None:
            root = n
        else:
            root = insert_avl(root,n)

        print("AVL(%d):"%i, end='')
        levelorder(root)
        print()