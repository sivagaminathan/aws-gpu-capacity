import boto3
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()
ec2 = boto3.client('ec2')

describe_instances = ec2.describe_instances()
# Only shows instances that are running
#print(describe_instances)

describe_regions = ec2.describe_regions()
print('-----------------------------')
region_names = [region['RegionName'] for region in describe_regions['Regions']]
print('Regions: ', region_names)

# Get all GPU Instances running in the region
get_gpu_instances = ec2.get_instance_types_from_instance_requirements(ArchitectureTypes = ['x86_64'], VirtualizationTypes = ['hvm'], InstanceRequirements={'AcceleratorTypes': ['gpu'], 'VCpuCount': {'Min': 1}, 'MemoryMiB': {'Min': 1}})

# Store the GPU instances in a list
gpu_instances = [instance['InstanceType'] for instance in get_gpu_instances['InstanceTypes']]

# If no GPU instances are found, get all instance type offerings for the 'region' or 'availability-zone' 
if not get_gpu_instances:
    print('No GPU instances found')

# For Each GPU instance, get the instance type offerings
# We make one API call for all GPU instance to reduce Amazon EC2 API calls
describe_instance_type_offerings = ec2.describe_instance_type_offerings(LocationType='region', Filters=[{'Name': 'instance-type', 'Values': gpu_instances}])

# Store the instance type offerings in a list 'InstanceType' and 'Region' 
instance_type_offerings = describe_instance_type_offerings["InstanceTypeOfferings"]
region_availability = [offering['Location'] for offering in describe_instance_type_offerings['InstanceTypeOfferings']]

# Returns this page for localhost:8000 (127.0.0.1:8000) 
@app.get("/", response_class = PlainTextResponse)
async def read_root():
    return "Welcome to the AWS EC2 GPU Instance Offering API \n " \
    "Available API endpoints are: \n " \
    "/gpu-instances/ \n " \
    "/instance-type-offerings/ \n " \
    "/gpu-instances/{gpu_instance_type} \n " \
    "/instance-type-offerings/{x} "

# Get all GPU instances running in the region
@app.get("/gpu-instances/")
async def get_gpu_instances():
    print("Getting GPU instances...", gpu_instances)
    return gpu_instances    

# Get all GPU instance type offerings for the region based on specified GPU instance type
@app.get("/instance-type-offerings/")
async def get_instance_type_offerings():
    print("Getting instance type offerings...", describe_instance_type_offerings)
    return describe_instance_type_offerings

# Get all GPU instance type offerings for the region based on specified GPU instance type
@app.get("/instance-type-offerings/{x}")
async def get_instance_type_offerings(x: str):
    print("Getting instance type offerings...", describe_instance_type_offerings)
    return {"message": "Test ", "x": x}

# Get all regions that runs specified GPU instance type
@app.get("/gpu-instances/{gpu_instance_type}")
async def get_gpu_instances(gpu_instance_type: str):
    flag = False
    return_records = {}
    for region in region_names:
        ec2 = boto3.client('ec2', region_name=region)
        #describe_availability_zones = ec2.describe_availability_zones()
        # Takes parameter Region 
        describe_instance_type_offerings = ec2.describe_instance_type_offerings(LocationType='availability-zone', Filters=[{'Name': 'instance-type', 'Values': gpu_instances}])
        for each_record in describe_instance_type_offerings['InstanceTypeOfferings']:
            for gpu_instance in gpu_instances:
                if gpu_instance_type == gpu_instance and each_record['InstanceType'] == gpu_instance:
                    availability_zone = each_record['Location']
                    if gpu_instance_type not in return_records:
                        return_records[gpu_instance_type] = []
                    return_records[gpu_instance_type].append(availability_zone)
                    flag = True
    if flag:
        return return_records
    else:
        return {"message": "No region offering GPU instance type found"}

# For Given Region, return all GPU instances offered in that region as a dictionary 
@app.get("/gpu-instances/region/{region}")
async def get_gpu_instances_in_region(region: str):
    flag = False
    return_records = {}
    ec2 = boto3.client('ec2', region_name=region)
    region = region.lower()
    dict_value = []
    # Takes parameter Region 
    describe_instance_type_offerings = ec2.describe_instance_type_offerings(LocationType='availability-zone', Filters=[{'Name': 'instance-type', 'Values': gpu_instances}])
    for each_record in describe_instance_type_offerings['InstanceTypeOfferings']:
        if region in each_record['Location']:
            instance_type = each_record['InstanceType']
            location = each_record['Location'] 

            if instance_type not in return_records:
                return_records[instance_type] = []
            return_records[instance_type].append(location)

            print(return_records.get(instance_type))
            #dict_value = []
            #return_records.append(availability_zone['ZoneName'])
            flag = True
    if flag:
        # This is the way to return it as a plain text response
        return return_records
    else:
        return {"message": "No GPU instance type found in the specified region"}




"""
  
# For Given Region, return all GPU instances offered in that region
@app.get("/gpu-instances/region/{region}", response_class=PlainTextResponse)
async def get_gpu_instances_in_region(region: str):
    flag = False
    return_records = []
    ec2 = boto3.client('ec2', region_name=region)
    region = region.lower()
    describe_availability_zones = ec2.describe_availability_zones()
    # Takes parameter Region 
    describe_instance_type_offerings = ec2.describe_instance_type_offerings(LocationType='availability-zone', Filters=[{'Name': 'instance-type', 'Values': gpu_instances}])
    for each_record in describe_instance_type_offerings['InstanceTypeOfferings']:
        #for availability_zone in describe_availability_zones['AvailabilityZones']:
        if region in each_record['Location']:
            new_string = each_record['InstanceType'] + " -in- " + region + " -zone- " + each_record['Location']
            return_records.append(new_string)
            return_records.append("\n")
            #return_records.append(availability_zone['ZoneName'])
            flag = True
    if flag:
        # This is the way to return it as a plain text response
        return "".join(return_records)
    else:
        return {"message": "No GPU instance type found in the specified region"}




describe_availability_zones = ec2.describe_availability_zones()
for availability_zone in describe_availability_zones['AvailabilityZones']:
    print('-----------------------------')
    print('RegionName: ', availability_zone['RegionName'])
    print('ZoneName: ', availability_zone['ZoneName'])

# TODO: Add more filters to the describe_instance_type_offerings API call to get more specific information about the GPU instances
Sufficient Account permissions required

describe_availability_zones = ec2.describe_availability_zones()
print('-----------------------------')
print('Availability Zones: ', describe_availability_zones['AvailabilityZones'])


# Describes the capacity block offerings for a specified instance type and count
describe_capacity_block_offerings = ec2.describe_capacity_block_offerings(InstanceType = 'p5en.48xlarge', InstanceCount = 1, CapacityDurationHours = 24)
print('-----------------------------')
print('Capacity Block Offerings: ', describe_capacity_block_offerings['CapacityBlockOfferings'])


# Capacity Manager metrics for a specified time range filtered by instance type
InstanceWeWant = {
        'Dimension': 'instance-family',
        'Comparison': 'equals',
        'Values': ['t2'] 
    }
get_capacity_manager_metric_data = ec2.get_capacity_manager_metric_data(MetricNames = ['reservation-unused-total-estimated-cost'], StartTime = '2023-01-01T00:00:00Z', EndTime = '2023-01-03T00:00:00Z', Period = 3600,
                                                                        FilterBy = InstanceWeWant)
print('-----------------------------')
print('Capacity Manager Metric Data: ', get_capacity_manager_metric_data['MetricDataResults'])

"""