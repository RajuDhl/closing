from collections import Counter

from Modules import room_count
from Modules import toga


def calculate(room_count_file, toga_file, total_co, total_stay, dnd, nsr, b2b, nscl, clean, day_use):
    error = []
    result_from_toga = toga.toga(toga_file)
    result_from_1c = room_count.room_count(room_count_file)
    for item in dnd:
        result_from_1c[int(item)] = 'dnd'
    for item in nsr:
        result_from_1c[int(item)] = 'nsr'

    diff_values = {key: result_from_1c[key] for key in result_from_1c if
                   key in result_from_toga and result_from_1c[key] != result_from_toga[key]}

    charged_co = sum(1 for value in result_from_1c.values() if value == 'dep')
    charged_stay = sum(1 for value in result_from_1c.values() if value == 'occ')
    charged_wc = sum(1 for value in result_from_1c.values() if value == 'wc')
    actual_co = int(total_co) - len(b2b) - len(nscl) - len(clean) + len(day_use)
    actual_stay = int(total_stay) - len(dnd) - len(nsr)

    if charged_co != actual_co:
        error.append(f'Departure should be {actual_co} but is {charged_co} in 1c\n')
    if charged_stay + charged_wc != actual_stay:
        error.append(f"Stay should be {actual_stay} but is {charged_stay + charged_wc} in 1c\n")
    error.append("<br><br>##########################")
    error.append("Please make following changes in toga")

    sorted_diff = {key: diff_values[key] for key in sorted(diff_values)}
    for key, value in sorted_diff.items():
        error.append(f"{key}: {value}")

    return error
