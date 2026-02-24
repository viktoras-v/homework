resource "aws_db_instance" "database" {
    allocated_storage = 5
    engine= "mysql"
    instance_class= "db.t3.micro"
#    username= "admin"
#    password= "notasecurepassword"
    username= var.db_username
    password= var.db_password
    skip_final_snapshot = true
}