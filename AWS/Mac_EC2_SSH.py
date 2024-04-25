import paramiko

#public Ip address or DNS hostname of EC2 instance

ec2_ip = "3.91.81.26"


#ssh key .pem file for authentication

key_file= "Mac_EC2.pem"

# username of EC2

ec2_username = "ec2-user"




# create SSH client

ssh_client = paramiko.SSHClient()

# automatically add host keys

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# connect to EC2 instance

ssh_client.connect(ec2_ip,username=ec2_username,key_filename=key_file)


# execute commands on EC2 instance

cmd = "ls"

try:
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read().decode())

except:
    print("command returned no op")


#close the SSH connection
ssh_client.close()


