#!/usr/bin/env python 3 

import pwd

for user in pwd.getpwall():
    print(user.pw_name)
    