from DataStructures.Tree import bst_node as bn

def insert_node(root, key, value):
    
    if root is None:
        return {
            "key": key,
            "value": value,
            "left": None,
            "right": None
        }
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    return root

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def default_compare(key, element):
   if key == bn.get_key(element):
      return 0
   elif key > bn.get_key(element):
      return 1
   return -1    
    
def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
        
    
    
    
    
    
    
    
    pass
def get():
    pass
def size():
    pass
