# Package example

from students import fees
from students.fees import current_status
import students.fees
import students.attendence

students.fees.current_status()
students.attendence.current_status()

print("")

students.fees.late_fine()
students.fees.fee_submitted()

students.attendence.percentage()
students.attendence.attendence_mark()

print("")

current_status()

print("")

fees.current_status()
fees.late_fine()

print("")

fees.exam()

# import module from sub-package 

import students.academy.exam as e
import students.academy.homework as h

e.exam()
e.percentage()
e.Division()

print("")

h.hw()
h.current_status()
h.time_taken()
