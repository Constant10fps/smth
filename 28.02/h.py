s = input().split()
st = []
for elem in s:
    if elem == "+":
        op_1 = st.pop()
        op_2 = st.pop()
        st.append(op_1 + op_2)
    elif elem == "-":
        op_1 = st.pop()
        op_2 = st.pop()
        st.append(op_2 - op_1)
    elif elem == "*":
        op_1 = st.pop()
        op_2 = st.pop()
        st.append(op_1 * op_2)
    else:
        st.append(int(elem))
print(st.pop())
