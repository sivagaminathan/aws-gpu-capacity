# AWS-GPU-CAPACITY

AWS GPU CAPACITY is a python program that queries for all gpu instances in a given region

## AWS LOGIN

```bash
aws login
```
to establish cloud console credentials 

## Usage

```python
python -m uvicorn GetInstances:app --reload
```

# Access Server at: "127.0.0.8000"

# /gpu-instances/
Returns a list of gpu instances in a given region : US-EAST
Example response: [dl1.24xlarge","g4ad.16xlarge"]

# /instance-type-offerings/ 
Filters only the GPU instances offered in a given region by instance type, location type and location
Example response: [{"InstanceType":"g6.4xlarge","LocationType":"region","Location":"us-east-1"},{"InstanceType":"g6.48xlarge","LocationType":"region","Location":"us-east-1"}]

# /gpu-instances/{gpu_instance_type} 
Returns a list of location info for a given gpu instance type for all regions 
Example response: {"g4ad.8xlarge":["eu-west-2c","eu-west-2a","eu-west-1c","eu-west-1b","eu-west-1a","ap-northeast-1a","ap-northeast-1c","ap-northeast-1d","ca-central-1a","ca-central-1b","eu-central-1b","eu-central-1a","us-east-1b","us-east-1a","us-east-1d","us-east-1c","us-east-2b","us-east-2c","us-east-2a","us-west-2b","us-west-2c","us-west-2a"]}

# instance-type-offerings/x 
Simple test to return "x" as an instance type 
Implementation for future results awaits here!

## Contributing 

Not open for public contributions
