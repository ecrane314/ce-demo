1. Remember tuples are immutable and lists not. Place tuples inside of lists for added capability
1. TODO For some reason, lists can be placed inside tuples, and updated. WHY?!?!?!
1. Immutable provides hints to developer and interpreter that this can't be changed.
1. tuple.__hash__() works but list.__hash__() is an error. If tuple contains a list, can't be hashed. I suppose the immutable part of the tuple is the pointer to the memorory space. If it points to the beginning of a list, then that pointer is still valid. 
1. list has many many more functions like push and pop, sort etc
1. zip() takes iterables and combines them into a tuple of pairs