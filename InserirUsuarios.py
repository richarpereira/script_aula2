#!/usr/bin/env python3

import subprocess

#define nome de usuario e senha do novo usuario

new_user_name = "Ainn_Zé_da_manga"
new_user_password = "password123"

#cria o usuario no sistema linux

subprocess.run(["sudo","useradd",new_user_name])
subprocess.run(["sudo","passwd",new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())

#input=f"{new_user_name\n{new_user_password}\n".encode())
