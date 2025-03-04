"""
Aspect	    Local Variable          	Global Variable	                Nonlocal Variable
Definition	Defined inside a function	Defined outside any function	Defined in an enclosing
                                                                        (but not global) scope
Scope	    Only accessible inside the   Accessible from anywhere in    Accessible inside nested
               function                       the script                     functions

Lifetime	Exists only during          Exists for the duration         Exists during the execution of
            function execution               of the program                  the enclosing function
Keyword 	No special keyword needed	Can be accessed directly,       Use nonlocal to modify the
                                            use global to modify        enclosing function's variable
Access	    Only inside the function	Anywhere in the program         Inside nested functions,
                                                                        not global scope
"""

