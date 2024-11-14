def selection_sort(arr):
    for i in range(len(arr)):
        m = arr[i]
        m_ind = i
        for j in range(i, len(arr)):
            if arr[j] < m:
                m = arr[j]
                m_ind = j
        holder = arr[i]
        arr[i] = m
        arr[m_ind] = holder
    
    return arr
