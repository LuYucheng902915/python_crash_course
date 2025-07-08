# 8-16. Imports:
# Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import printing_functions
import printing_functions as pf

# from printing_functions import *
# 这是一种不推荐的引用，会导致静态分析工具失效等问题。
from printing_functions import print_models, show_completed_models
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

# from printing_functions import print_models as pm, show_completed_models as scm
# 可以写一行，格式化工具会变成两行。
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models_0: list[str] = []
printing_functions.print_models(unprinted_designs, completed_models_0)
printing_functions.show_completed_models(completed_models_0)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models_1: list[str] = []
print_models(unprinted_designs, completed_models_1)
show_completed_models(completed_models_1)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models_2: list[str] = []
pm(unprinted_designs, completed_models_2)
scm(completed_models_2)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models_3: list[str] = []
pf.print_models(unprinted_designs, completed_models_3)
pf.show_completed_models(completed_models_3)

# test_function(completed_models_0)
