
# Create and run container for lab
docker build -t my_ubuntu .
docker run -d -p 22:22 --rm my_ubuntu

1
# Install NGINX with role
ansible-playbook -i ~/homework/Homework_20/1/inventory ~/homework/Homework_20/1/install_nginx.yml

2
# Utiliztion of variables upon app deploy
ansible-playbook -i inventory variable_utilization.yml -l prod

3
# Using secrets
ansible-playbook -i inventory configure_app.yml --ask-vault-pass -l dev
password "test"

4
# Error handling
ansible-playbook -i inventory error_handle.yml
