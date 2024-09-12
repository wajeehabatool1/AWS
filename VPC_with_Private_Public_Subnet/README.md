# VPC With Private and Public Subnet in Production
![image](https://github.com/user-attachments/assets/a0768f7a-53a2-4ab9-a330-4be315679705)
## Prerequisites

### AWS Account
- Ensure you have an active AWS account.

### Proper Access
- Verify that you have appropriate permissions to access and manage VPC (Virtual Private Cloud) and related services.
- 
## Concepts Used
- **VPC (Virtual Private Cloud)**
- **Auto Scaling Group**
- **Launch Templates**
- **Load Balancer**
- **Target Group**
- **Bastion Host**

## Create VPC
- **For Resources to Create** Choose **VPC and more** beacuse AWS automatically provides configurations like subnets, route tables, and an internet gateway etc rather than setting it up manually.
- 2 Availbilty Zone 
- 2 Public Subnets
- 2 Private Subnets
- 1 NAT Gateway per Availbility Zone
- VC endpoint None
  
**The pictorial representation of VPC Configuration**

![image](https://github.com/user-attachments/assets/b40dd64f-901a-43a5-9712-9754a2927d9d)
## Create Launch Templates
Launch template is used in Auto Scaling to automate the process of building ec2 instances with predefined configurations
- Ubuntu Linux distribution for ec2 instances with instance type of own choice
- adding key pair for shh login 
- Added Security Group should have these inbound traffic rules that is **ssh type on port 22 for ssh login for devlopers** and **custom tcp type with port 8000 or of own choice for load balancers to forward the incoming traffic to private ec2 instances** with source type **anywhere**
- select the newly created VPC 
![image](https://github.com/user-attachments/assets/429b7dad-13f5-4abd-9aaa-15d98f01a324)

## Create Auto Scaling Group

- Adding recently created launch template
- Select the desired VPC
- Since ec2 instances are private , we will select private subnets for both availibilty Zones

  ![image](https://github.com/user-attachments/assets/acd84261-6987-4751-8348-424044c16cf1)
- not creating any internal load balancer
- Desired Capacity is 2 since we have 2 availibilty zone
- Minimum scaling capacity is 1
- maximum scaling capacity is 4

![image](https://github.com/user-attachments/assets/38b09c83-d819-4a87-808f-01267f977518)

- Auto Scaling Group has launched automatically two ec2 instances, one in each availibility zone

![image](https://github.com/user-attachments/assets/14a968fb-7408-4a3f-ba09-53b8ba209a4e)

- The launched ec2 instances dont have a public ip address, because they are in private subnet and they have to be secure

![image](https://github.com/user-attachments/assets/33a2c95b-38d4-4fcc-96b3-bcbe9ba58f5b)

## Create Target Groups
Target groups are created for load balancers to define and manage which specific instances or resources receive traffic

- target is ec2 instances
- load balancer is going to be of **Application type** , therefore selecting the protocol of accessing as **Http** and ec2 port **8000** will be open for receiving request from load balancer therefore setting port to **8000**
- selecting **recently created VPC** from option
- From available instance, selecting the two ec2 instances with no public IP available beacuse of the private subnet assigned to both of them
- clicking on include as pending below to finalized the selected ec2 instances
  Target Group is created
  ![image](https://github.com/user-attachments/assets/427dc48d-d843-4218-b0e1-0ed9e49dc8b7)


## Create Load Balancer
Load balancer will send the recieved traffic to the target groups
- selecting application based load balancer
- load balancer is internet facing to recieve traffic from the outside world
- select the VPC , recently created one
- select the both availibilty zones and select the public subnets for both availibilty zones
-  select the secuirty group , make sure the port on which load balancer is receiving traffic should be exposed to outside. Set type to **Http with port 80 and source anywhere**

 Load balancer is active
 
  ![image](https://github.com/user-attachments/assets/928288ab-a427-4d01-9756-ecb47ecab300)

## Create Bastion Host
Bastion host acts as gateway to access private networks
- Create a ec2 instance manually with a public ip and security group of inbound traffic type ssh with port 22 and source everywhere 
## Accessing ec2 instances in private subnets through Bastion Host
Since ec2 instances are private , we will copy the ssh key-pair file that we use in launch template to our bastion host
Go to the CLI of your machine where you have stored the ssh key-pair and run this comand 
```bash
scp-i/path/to/directory/bastion.pem /path/to/directory/Target.pem ubuntu@0.0.0.0:/home/ubuntu
```
- bastion.pem is the key pair of bastion host
- Target.pem is the key pair of private ec2 instances
- 0.0.0.0 is the public ip of the host
- /home/ubuntu is the directory in bastion host where you want to safe copy your key pair
- bastion host will access the ec2 instaces through ssh using key pair and private ips of instances


```bash
 ssh -i Target.pem ubuntu@0.0.0.0
```
- now , we  will be able to enter into ec2 instance and run the server
- we will add a file named index.html in both ec2 instances and run a simple python server on both instances so that we will be able to see that web page when accessing the instances through load balancer
  
 ```bash
 python3 -m http.server 8000
``` 
- to access the servers , go to load balancer and copy the DNS name and paste in URL to access the server

 here we can see , we are able to access the servers , and they are serving the web page
 Note: The web page file is present in the current folder
 
   ![image](https://github.com/user-attachments/assets/d3b3bf38-8e81-4d18-b459-eb702a058160)

   Server is receving request 

![image](https://github.com/user-attachments/assets/f7c0cfa2-d998-467b-9fcd-67308f16cd7c)

Load balancer is keeping check on the server health , here we can see both servers are up and running 

  ![image](https://github.com/user-attachments/assets/26dc9d12-a27b-4b2d-9bfc-3ed95c7615fd)

