from modules.all_states import AdminStates, BasicStates, SendStates

class New_Class:
    a = 1082308
    h = 21392832

def get_all_values(class_):
    variables = vars(class_)
    save = list(variables)
    seacher_filter = "__dict__"
    # print(save)
    if seacher_filter not in save:
        seacher_filter = "__doc__"
    result = save[1:save.index(seacher_filter)]
    variable = [str(variables[num]) for num in result]
    return variable
    


classes = [AdminStates, BasicStates, SendStates, New_Class]

print("\n".join([", ".join(get_all_values(class_obj)) for class_obj in classes]))
# get_all_values(AdminStates)
# list = [1 for i in range(0, 5)]
# print(list)
# for i in list(5):
   