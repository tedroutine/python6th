# 사용자 입력으로 리스트 만들기

user_input_list = []
num_elements = int(input("Enter number of element: "))
for i in range(num_elements):
    user_input_list.append(input("enter element:"))

print(user_input_list)
for elements in user_input_list:
    print(elements)