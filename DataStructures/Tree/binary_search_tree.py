from DataStructures.Tree import bst_node 

def new_map ():
    
    return {"root": None}

def insert_node(root, key, value):
    if root is None:
        return {"key": key, "value": value, "left": None, "right": None}

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    return root


def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
    
def size_tree(tree):
    if tree is None:
        return 0
    return 1 + size_tree(tree["left"]) + size_tree(tree["right"])

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
        

def size_node(root):
    if root is None:
        return 0
    else:
        return 1 + size_node(root["left"]) + size_node(root["right"])
        
def size (my_bst):
    if my_bst["root"] is None:
        return 0
    else:
        return size_node(my_bst["root"])
    
def get_min_node(root):
    if root is None:
        return None
    else:
        current = root
        while current["left"] is not None:
            current = current["left"]
        return current["key"]
    
def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_min_node(my_bst["root"])

def get_max_node(root):
    if root is None:
        return None
    else:
        current = root
        while current["right"] is not None:
            current = current["right"]
        return current["key"]
    
def get_max(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_max_node(my_bst["root"])
    
def delete_min_tree(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    return root

def delete_min(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["right"]
    root["right"] = delete_max_tree(root["right"])
    return root    

def delete_max(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

