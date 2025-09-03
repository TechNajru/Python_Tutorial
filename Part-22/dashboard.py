# Main Module in Which all other modules are call

# import fee_submitted, current_status function from fees
from attendence import *
from fees import fee_submitted, current_status
import attendence
import fees


# import all functions from attendence module


fee_submitted()
# Current_status is in both fees and attendence so it show the function from module which added or call at last
current_status()

attendence_mark()
percentage()
modify()

print("")


attendence.current_status()
fees.current_status()

attendence.attendence_mark()
attendence.percentage()
attendence.modify()

fees.fee_submitted()
fees.late_fine()
