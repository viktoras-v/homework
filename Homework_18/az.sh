#!/bin/bash

# Variables
count_default="1"
rgroup_default="my_group"
vm_name_default="az-test"
username_default="azureuser"
image_default="Ubuntu2404"
size_default="Standard_D2s_v5"
sshkey_default="~/.ssh/id_ed25519.pub"

# Functions
create_vm () {
    echo "Provisioning new vm $2"
    echo "az vm create --resource-group $1 --name $2 --image $3 --ssh-key-values $4 --admin-username $5 --size $6"
    echo
    az vm create --resource-group $1 --name $2 --image $3 --ssh-key-values $4 --admin-username $5 --size $6
    
}

delete_vm () {
    echo "Deleteng vm $2"
    echo "az vm delete --resource-group $1 --name $2"
    echo
    az vm delete -n $2 -g $1
}

# Menu
echo "Wellcome to az-vm wrapper"
read -p "Select action: l-login c - create, d - delete " action

# Login action
if [ "$action" == "l" ]; then
az login --use-device-code
fi

# Create VM
if [ "$action" == "c" ]; then
echo "Hint: Press enter for default value."
read -e -i "$count_default" -p "Enter vm count: " input
count=${input:-$count}
for ((i=1; i<=count; i++));
do
unset input
read -e -i "$rgroup_default" -p "Enter resource group: " input
rgroup=${input:-$rgroup_default}
unset input
read -e -i "$vm_name_default" -p "Enter vm name: " input
vm_name=${input:-$vm_name_default}
unset input
read -e -i "$username_default" -p "Enter username: " input
username=${input:-$username_default}
unset input
read -e -i "$image_default" -p "Enter image: " input
image=${input:-$image_default}
unset input
read -e -i "$size_default" -p "Choose size: Standard_D2s_v3 or Standard_D4s_v3 or Standard_E2s_v3: defaut is " input
size=${input:-$size_default}
if [ "$size" != "Standard_D2s_v5" ] && [ "$size" != "Standard_D4s_v3" ] && [ "$size" != "Standard_E2s_v3" ] ; then
    echo "Wrond size. Bye!"; 
    exit 1;
fi
unset input
read -e -i "$sshkey_default" -p "Enter path to ssh key: " input
sshkey=${input:-$sshkey_default}
create_vm $rgroup $vm_name $image $sshkey $username $size
done
fi

# Delete VM
if [ "$action" == "d" ]; then
echo "Hint: Press enter for default value."
read -e -i "$vm_name_default" -p "Enter vm name: " input
vm_name=${input:-$vm_name_default}
unset input
read -e -i "$rgroup_default" -p "Enter resource group: " input
rgroup=${input:-$rgroup_default}
delete_vm $rgroup $vm_name
fi

# Error input
if [ "$action" != "c" ] && [ "$action" != "d" ] && [ "$action" != "l" ] ; then 
    echo "Wrond action. Bye!"; 
    exit 1;
fi