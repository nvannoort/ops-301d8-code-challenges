#!/usr/bin/env python3

# Script Name:                  Ops301d8 Day 13
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/15/2023
# Purpose:                      adding users in powershell

# Set user details

$userGivenName = "Franz"
$userSurname = "Ferdinand"
$userTitle = "TPS Reporting Lead"
$userCompany = "GlobeX USA"
$userCity = "Springfield"
$userState = "OR"
$userDepartment = "TPS Department"
$userEmail = "ferdi@GlobeXpower.com"
$userUsername = $userEmail.Split("@")[0]
$userOffice = "Springfield, OR office"

# Create the new user
New-ADUser `
    -SamAccountName $userUsername `
    -UserPrincipalName $userEmail `
    -Name "$userGivenName $userSurname" `
    -GivenName $userGivenName `
    -Surname $userSurname `
    -Title $userTitle `
    -Company $userCompany `
    -Department $userDepartment `
    -EmailAddress $userEmail `
    -City $userCity `
    -State $userState `
    -Office $userOffice `
    -Enabled $True `
    -PassThru

Write-Output "User $userUsername has been created."