#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    answer = None
    """
    YOUR CODE HERE
    """

    for i in range(length):
        try:
            
            if hash_table_retrieve(ht, weights[i]) == None:
                hash_table_insert(ht, weights[i], [i, weights[i], limit - weights[i]])
            
            if weights[i] + hash_table_retrieve(ht, weights[i])[1] == limit and hash_table_retrieve(ht, weights[i])[0] != i :
                answer = (i, hash_table_retrieve(ht, weights[i])[0])

            if hash_table_retrieve(ht, limit - weights[i]) != None and limit - weights[i] != weights[i]:
               answer = (hash_table_retrieve(ht, weights[i])[0], hash_table_retrieve(ht, limit - weights[i])[0])

        except:
            continue

    return answer



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
