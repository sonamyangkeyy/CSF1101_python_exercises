with open('Challange Ex/fruit_transactions.txt','r') as file:
    data = file.readlines()

    length = len(data)
    print(f"the length of data is {length}")

    first_line = data[0]
    print(f'the first line is: {first_line}')

    all_dict_data = []
    for line in data:
        line_dictionary = {}
        cleaned_line = line.replace('/n','')
        splitted_line = cleaned_line.split(',')

        line_dictionary['name'] = splitted_line[0]
        line_dictionary['action'] = splitted_line[1]
        line_dictionary['quantity'] = int(splitted_line[2])
        line_dictionary['item'] = splitted_line[3]
        line_dictionary['price'] = float(splitted_line[4])

        all_dict_data.append(line_dictionary)

total_sales = sum(item['quantity'] * item['price'] for item in all_dict_data)
print(f'total sales from sold transaction: ${total_sales:2f}')

fruit_counts = {}
for item in all_dict_data:
    fruit = item['item']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

most_popular_fruit = max(fruit_counts, key=fruit_counts.get)
most_popular_fruit_count = fruit_counts[most_popular_fruit]

print(f'the most popular fruit is: {most_popular_fruit}with {most_popular_fruit_count} transaction')

total_value = sum(item['quantity'] * item['price'] for item in all_dict_data)
total_transaction = len(all_dict_data)
average = total_value / total_transaction
print(f'the average transactiom value:{average: .2f}')

spender = {}
for item in all_dict_data:
    if item['action'] == 'bought' :
        if item['name'] in spender:
            spender[item['name']] += item['quantity'] * item['price']
        else: 
            spender[item['name']] = item['quantity'] * item['price']

biggest_spender = max(spender, key=spender.get)
total_amount = spender[biggest_spender]
print(f'biggest spender is: {biggest_spender} with ${total_amount: .2f}')

summary = (
    f'total sale: ${total_sales}\n'
    f'popular fruit: {most_popular_fruit}\n'
    f'average value: {average}\n'
    f'biggest spender: {biggest_spender}\n'
)

with open('transaction_summary.txt','w') as summary_file:
    summary_file.write(summary)
    print(f'the summary has been written in "transaction_summary.txt".')
        