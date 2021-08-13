



def info_getter(**kwargs):
    data = {}
    for k, v in kwargs.items():
        data[k] = v
    return data 

def test_info_getter():
    # provide positive test for function info_getter

    # prove that when info_getter has a key, value pair passed
    # it will return a dictionary containing that key value pair
    assert info_getter(lunch="yes please") == {"lunch": "yes please"}
    assert info_getter(lunch="yes please", dinner="maybe later") == {"lunch": "yes please", "dinner": "maybe later"}

    
def test_info_getter_fail():
    assert info_getter(lunch="not yet") != {"lunch": "yes please"}
