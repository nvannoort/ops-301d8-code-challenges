#!/bin/bash

while true; do
    clear
    echo "Please Make a Choice"
    echo "1. Hello world (prints “Hello world!” to the screen)"
    echo "2.Ping self (pings this computer’s loopback address)"
    echo "3. IP info (print the network adapter information for this computer)"
    echo "4. Exit"
    read choice

    if [[ $choice == 1 ]]; then
        echo "Hello World"
        # The -p option is used with the read command to display a prompt to the user and wait for them to enter input.
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        echo "Pinging the Computer you are on"
        ping 127.0.0.1
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
        echo "This is the IP info you requested"
        ip a
        read -p "Press Enter to continue"
    elif [[ $choice == 4 ]]; then
        echo "See ya later!"
        exit 0
    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done