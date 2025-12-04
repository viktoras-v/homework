#!/bin/bash

count="1"
rgroup="my_group"
vm_name="az-test"
username="azureuser"
image="Ubuntu2404"
size="Standard_D2s_v5"
sshkey="~/.ssh/id_ed25519.pub"

create_vm () {
    az vm create --resource-group $1 --name $2 --image $3 --ssh-key-values $4 --admin-username $5 --size $6
}

delete_vm () {
    az vm delete -n $2 -g $1
}

echo "Wellcome to az-vm wrapper"
read -p "Select action: l-login c - create, d - delete " action

if [ "$action" == "l" ]; then
az login --use-device-code
fi

if [ "$action" == "c" ]; then
echo "Hint: Press enter for default value."
read -e -i "$count" -p "Enter vm count: " input
count=${input:-$count}
for i in {1..$count}
do
read -e -i "$rgroup" -p "Enter resource group: " input
rgroup=${input:-$group}
read -e -i "$vm_name" -p "Enter vm name: " input
vm_name=${input:-$vm_name}
read -e -i "$username" -p "Enter username: " input
username=${input:-$username}
read -e -i "$image" -p "Enter image: " input
image=${input:-$image}
read -e -i "$size" -p "Choose size: Standard_D2s_v3 or Standard_D4s_v3 or Standard_E2s_v3: defaut is " input
size=${input:-$size}
if [ "$size" != "Standard_D2s_v3" ] && [ "$size" != "Standard_D4s_v3" ] && [ "$size" != "Standard_E2s_v3" ] ; then
    echo "Wrond size. Bye!"; 
    exit 1;
fi
read -e -i "$sshkey" -p "Enter path to ssh key: " input
sshkey=${input:-$sshkey}
echo "Provisioning new vm $name"
create_vm $rgroup $vm_name $image $sshkey $username $size
done
fi


if [ "$action" == "d" ]; then
echo "Hint: Press enter for default value."
read -e -i "$vm_name" -p "Enter vm name: " input
vm_name=${input:-$vm_name}
read -e -i "$rgroup" -p "Enter resource group: " input
rgroup=${input:-$rgroup}
echo "Deleting vm $name"
delete_vm $rgroup $vm_name
fi

if [ "$action" != "c" ] && [ "$action" != "d" ] && [ "$action" != "l" ] ; then 
    echo "Wrond action. Bye!"; 
    exit 1;
fi