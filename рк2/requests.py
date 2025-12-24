# from operator import itemgetter
# import data
#
# def get_A1():
#     return []
#
# def get_A2():
#     return []
#
# def get_A3():
#     return []










from operator import itemgetter
import data

def get_A1():
    """Возвращает список всех связанных музыкантов и оркестров, отсортированный по названию оркестра."""
    one_to_many = [(m.name, m.salary, o.name)
                   for o in data.orchestras
                   for m in data.musicians
                   if m.orchestra_id == o.id]
    sorted_result = sorted(one_to_many, key=itemgetter(2))
    return sorted_result

def get_A2():
    """Возвращает список оркестров с суммарной зарплатой музыкантов, отсортированный по сумме."""
    one_to_many = [(m.name, m.salary, o.name)
                   for o in data.orchestras
                   for m in data.musicians
                   if m.orchestra_id == o.id]
    res = []
    for o in data.orchestras:
        orch_musicians = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(orch_musicians) > 0:
            total_salary = sum(m[1] for m in orch_musicians)
            res.append((o.name, total_salary))
    sorted_res = sorted(res, key=itemgetter(1), reverse=True)
    return sorted_res

def get_A3():
    """Возвращает словарь: название оркестра — списки музыкантов, играющих в нем, с фильтром по названию."""
    # Временный список связывающий оркестры и музыкантов
    many_to_many_temp = [
        (o.name, mo.orchestra_id, mo.musician_id)
        for o in data.orchestras
        for mo in data.musicians_orchestras
        if o.id == mo.orchestra_id
    ]
    # Полный список: музыкант + оркестр
    many_to_many = [
        (m.name, m.salary, o_name)
        for o_name, o_id, m_id in many_to_many_temp
        for m in data.musicians
        if m.id == m_id
    ]
    filtered_orchestras = [name for name in set(d.name for d in data.orchestras) if 'оркестр' in name]
    res = {}
    for orchestra_name in filtered_orchestras:
        musicians_in_orchestra = list(filter(lambda i: i[2] == orchestra_name, many_to_many))
        musician_names = [m[0] for m in musicians_in_orchestra]
        res[orchestra_name] = musician_names
    return res