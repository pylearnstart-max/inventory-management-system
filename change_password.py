def change_password_screen(service, username):


    print("\n================================")
    print("       CHANGE PASSWORD")
    print("================================")


    old_password = input(
        "Enter Old Password: "
    )


    new_password = input(
        "Enter New Password: "
    )



    result = service.change_password(
        username,
        old_password,
        new_password
    )



    if result:

        print(
            "\nPassword Changed Successfully"
        )


    else:

        print(
            "\nOld Password Incorrect"
        )