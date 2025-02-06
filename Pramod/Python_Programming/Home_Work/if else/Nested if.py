"""
if cond1:
    code
    if cond2:
       code
       if cond3:
          code
       else
          code
    else
       code
else:
    code
"""
# write a python code to simulate the interview process with the help nested if condition
round1="pass"
round2="fail"
round3="pass"

if round1=="pass":
    print("you have cleared in first round")

    if round2=="pass":
        print("you have cleared in second round")

        if round3=="fail":
            print("you have cleared in third rround")

        else:
            print("Congracts cleared all round")
    else:
        print("you have not cleared in second round")
else:
    print("you have not cleared in first round")


