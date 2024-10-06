from collections import Counter

import toga, room_count

toga_file = 'toga.xlsx'
rc_file = 'rc.xlsx'

result_from_toga = toga.toga(toga_file)
result_from_1c = room_count.room_count(rc_file)


# Find differences
diff_values = {key: (result_from_1c[key], result_from_toga[key]) for key in result_from_1c if key in result_from_toga and result_from_1c[key] != result_from_toga[key]}


print(diff_values)


