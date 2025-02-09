from typing import List, Set, Tuple, Dict, Optional, Union
from pydantic import BaseModel, PositiveInt
from datetime import datetime

### By TypeHint, IDE can give further helps

# Original genric type List hinting
def func1(l: list):
    for i in range(len(l)):
        print("List %i : %s" % (i, l[i]))

### Type hint with typing Library(Basically None-Safe(Null-Safe?))
# List only with String member
def func2(l: List[str]):    
    tmp = ""
    for i in l:
        tmp += i
    print(tmp)

# For tuple or set
def func3(t: Tuple[int, int, str], s: Set[bytes]): 
    return t, s

# For Dict : Dict with string key and float value
def func4(d: Dict[str, float]):
    pass

# For Class
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

# Escape Null Safety
def func5(name: Optional[str] = None):
    if name is None:
        print("name is NULL")
    else:
        print("name is %s" % name)

# Pydantic Hint
class User(BaseModel):
    id: int
    name: str = "John Doe"
    #signup_ts: datetime | None # Supported from python 3.10
    signup_ts: Optional[datetime] = None
    signup_ts2: Union[datetime, None]
    signup_ts3: Union[datetime, str, None]
    tastes: Dict[str, PositiveInt]



