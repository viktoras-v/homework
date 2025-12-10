1
docker build -t my_ubuntu .
docker run -d -p 22:22 --rm my_ubuntu
ansible-playbook -i ~/homework/Homework_20/1/inventory ~/homework/Homework_20/1/install_nginx.yml

2
ansible-playbook -i inventory variable_utilization.yml -l prod

3
ansible-playbook -i inventory configure_app.yml --ask-vault-pass -l dev
password "test"



