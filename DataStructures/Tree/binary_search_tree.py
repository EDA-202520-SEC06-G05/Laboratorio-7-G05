from DataStructures.Tree import bst_node 

def new_map ():
    
    return {"root": None}

def default_compare (key, element):
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1

def get_node(root,key):
    
    if root is None:
        return None
    if bst_node.get_key(root) == key:
        return root
    elif bst_node.get_key(root) < key:
        return get_node(root["right"], key)
    elif bst_node.get_key(root) > key:
        return get_node(root["left"], key)
    

def get (my_bst, key):
    if my_bst["root"] == None:
        return None
    else:
        node = get_node(my_bst["root"], key)
        if node is None:
            return None
        else: 
            return bst_node.get_value(node)