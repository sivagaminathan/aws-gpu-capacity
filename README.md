# AWS-GPU-CAPACITY

A Web application built using FastAPI in python to get gpu capacity across AWS regions and data centers and availability zones

## AWS LOGIN
Requires AWS cloud credentials to query ec2 
```bash
aws login
```
Follow the instructions on the AWS Oath page to provide login info. 
These credentials will be shared to the local machine for a set period of time

## Usage
To run the app, please use the following command

```python
python -m uvicorn GetInstances:app --reload
```

## API Endpoints  
```
# Access Server at: "127.0.0.8000"

Response:
Welcome to the AWS EC2 GPU Instance Offering API 
 Available API endpoints are: 
 /gpu-instances/ 
 /instance-type-offerings/ 
 /gpu-instances/{gpu_instance_type} 
 /instance-type-offerings/{x} 
```

##  Get GPU instances by region
```
# /gpu-instances/
Example response:
[
  "dl1.24xlarge",
  "g4ad.16xlarge",
  "g4ad.2xlarge",
  "g4ad.4xlarge",
  ...,
  "p6-b200.48xlarge"
]
```
## Get Instance Type offerings by region filtered to GPU instances only
```
# /instance-type-offerings/ 
Example response:
[
  {
    "InstanceType": "g6.4xlarge",
    "LocationType": "region",
    "Location": "us-east-1"
  },
  {
    .............,
  },
  {
    "InstanceType": "g6.48xlarge",
    "LocationType": "region",
    "Location": "us-east-1"
  }
]
```
## Get Location info for a specific GPU instance type across all regions 
```
# /gpu-instances/{gpu_instance_type} 
Example response for call /gpu-instances/g4ad.8xlarge:
{
  "g4ad.8xlarge": [
    "eu-west-2c",
    "eu-west-2a",
    "eu-west-1c",
    "eu-west-1b",
    "eu-west-1a",
    "ap-northeast-1a",
    "ap-northeast-1c",
    "ap-northeast-1d",
    "ca-central-1a",
    "ca-central-1b",
    "eu-central-1b",
    "eu-central-1a",
    "us-east-1b",
    "us-east-1a",
    "us-east-1d",
    "us-east-1c",
    "us-east-2b",
    "us-east-2c",
    "us-east-2a",
    "us-west-2b",
    "us-west-2c",
    "us-west-2a"
  ]
}
```
## Test and Future Implementation
```
# instance-type-offerings/x 
This is a test run! 
Implementation for future results await here!
```

## Contributing 

Not open for public contributions
