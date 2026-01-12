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


# Access Server at: "127.0.0.8000"

Response:
Welcome to the AWS EC2 GPU Instance Offering API 
 Available API endpoints are: 
 /gpu-instances/ 
 /instance-type-offerings/ 
 /gpu-instances/{gpu_instance_type} 
 /instance-type-offerings/{x} 

# /gpu-instances/
Returns a list of gpu instances in a given region : US-EAST
Example response:
[
  "dl1.24xlarge",
  "g4ad.16xlarge",
  "g4ad.2xlarge",
  "g4ad.4xlarge",
  "g4ad.8xlarge",
  "g4ad.xlarge",
  "g4dn.12xlarge",
  "g4dn.16xlarge",
  "g4dn.2xlarge",
  "g4dn.4xlarge",
  "g4dn.8xlarge",
  "g4dn.xlarge",
  "g5.12xlarge",
  "g5.16xlarge",
  "g5.24xlarge",
  "g5.2xlarge",
  "g5.48xlarge",
  "g5.4xlarge",
  "g5.8xlarge",
  "g5.xlarge",
  "g6.12xlarge",
  "g6.16xlarge",
  "g6.24xlarge",
  "g6.2xlarge",
  "g6.48xlarge",
  "g6.4xlarge",
  "g6.8xlarge",
  "g6.xlarge",
  "g6e.12xlarge",
  "g6e.16xlarge",
  "g6e.24xlarge",
  "g6e.2xlarge",
  "g6e.48xlarge",
  "g6e.4xlarge",
  "g6e.8xlarge",
  "g6e.xlarge",
  "gr6.4xlarge",
  "gr6.8xlarge",
  "p3.16xlarge",
  "p3.2xlarge",
  "p3.8xlarge",
  "p3dn.24xlarge",
  "p4d.24xlarge",
  "p4de.24xlarge",
  "p5.48xlarge",
  "p5en.48xlarge",
  "p6-b200.48xlarge"
]

# /instance-type-offerings/ 
Filters only the GPU instances offered in a given region by instance type, location type and location
Example response:
[
  {
    "InstanceType": "g6.4xlarge",
    "LocationType": "region",
    "Location": "us-east-1"
  },
  {
    "InstanceType": "g6.48xlarge",
    "LocationType": "region",
    "Location": "us-east-1"
  }
]

# /gpu-instances/{gpu_instance_type} 
Returns a list of location info for a given gpu instance type for all regions 
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
# instance-type-offerings/x 
Simple test to return "x" as an instance type 
Implementation for future results awaits here!
```

## Contributing 

Not open for public contributions
