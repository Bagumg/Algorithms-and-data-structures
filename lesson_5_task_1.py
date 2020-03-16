from collections import OrderedDict


# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


data = OrderedDict()
firm_count = int(input('Input firms amount: '))
for i in range(firm_count):
    data[input('Input firm name: ')] = [
        int(input('First quarter income: ')),
        int(input('Second quarter income: ')),
        int(input('Third quarter income: ')),
        int(input('Fourth quarter income: '))
    ]
annual_income = (list(sum(v) for v in data.values()))
mid_annual_income = (int(sum(list(sum(v) for v in data.values())) / firm_count))

hi = []
lo = []
for k, v in data.items():
    if sum(v) <= mid_annual_income:
        lo.append(k)
    elif sum(v) > mid_annual_income:
        hi.append(k)

print('Middle annual income from all firms: ', mid_annual_income)
print('Firms whose annual income is higher than middle income ', hi)
print('Firms whose annual income is lower than middle income ', lo)


