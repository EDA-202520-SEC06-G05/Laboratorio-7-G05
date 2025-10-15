from DataStructures.Tree import bst_node 

def new_map ():
    
    return {"root": None}

def default_compare (key, element):
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1

def get_node(root, key):
    
    if root["left"] == None and root["right"] == None:
        if root["key"] == key:
            return root 
        else: 
            return None
        
    elif root["left"] == None and root["right"] != None:
        get_node(root["right"], key)
    elif root["left"] != None and root["right"] == None:
        get_node(root["left"],key)
    else:
        get_node(root["left"],key)
        get_node(root["right"], key)
        
    return None

def get (my_bst, key):
    return get_node(my_bst, key)