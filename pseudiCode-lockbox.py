hello this is  a little insight of what i think regarding lockboxes i hope it helps
someone. during an interview one might be called upon to answer many programming
 questioms. believe me having a mental image of any problem is the best u can do
for urself in an an interview as well as as in ur carrer as a software engineer. code are objects!

Consider a world W (list of list), where every house H (a list) is unbreakable, by any known advanced
technology including nuclear weapon.
In W, there are persons Mr A, B, C, D.
NOTE:
    1. if Mr A close his house with a padlock and forgets the key inside then, by hypthesis, Mr A can 
       never have access to his house Again!
    2. Assuming Mr A closes his house and gave the key to Mr B. He promises to take it back when he returns, Mr B keeps the key in a drawer. well, after a while Mr B closed, his house then gave his key to Mr C, who inturn gave his own house key to Mr D and left for a walk. During this period f Mr A returns, the question then arises, *who should Mr A go to collect his key? (bear in mind mr A may not know Mr C and D)
    *So for Mr A to get his Key back, the following condition has to be met*
    (a).Mr D has not gone out
        unlock = [0] or
        unlock = set([0])
    (b). mr A goes to Mr B, Mr B takes Mr A to Mr C and if Mr C has returned from his wark, will take both Mr A and Mr B to Mr D
    for house_id, H in enumerate(W):
        for key in H:

    (c). No key belonging to the same house house_id can be found in the same house. otherwise u can't enter ur house, ever Again.
    (d) the number of houses Mr A has to visit must not exceed the number of house from Mr B to Mr D, this number cant be bigger than the world itself.
    (e). finaly if Mr C took his key as well as Mr B's key and gave to Mr D, then Mr B will recieve his Key directly from Mr D withour having to take it from Mr C.

            if key < len(W) // W means world remember
            if key != house_id // No house contains its own key
            if key not in unlocked // if Mr D does not have Mr both Mr C and Mr B's key or possibly Mr A's
                unlocked.append(key) // list
                or
                unlocked.add(key) // set
    (e) However if Mr D has all the keys of Mr A, B, C. This will happen in the rare case where Mr B took his key as well as Mr A' and gave to Mr C and Mr C to his key as well as Mr B's and Mr A's and gave to Mr D. then each can collect their keys and open their House directly else the will waite for each person to open their house a d bring out each persons key consecutively'
    if len(unlocked) = len(W):
        return False
    return True


here is the nain Code

from typing import List
def CanUnlockBoxes(World: List[List[int]] =[]) -> bool:
    if not World:
        return False

    DHouse = [0] // unlocked

    for myHouseKey, House in enumerate(World):
        for key in House:
            if not key in DHouse and key < len(World) and key != myHouseKey:
                Dhouse.append(key) // this line says if A's key is not in B' or C's then its in D's House

    if len(Dhouse) != len(World):
        return False // cant open somr houses
    return True
