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

## Target Groups
Target groups are created for load balancers to define and manage which specific instances or resources receive traffic







