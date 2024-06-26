### AWS Redshift Cluster Configuration in python
import boto3

# Initialize a session using Amazon Redshift
client = boto3.client('redshift', region_name='us-east-1')

# Create Redshift Cluster
response = client.create_cluster(
    ClusterIdentifier='my-redshift-cluster',
    NodeType='dc2.large',
    MasterUsername='vivekraj',
    MasterUserPassword='********',
    NumberOfNodes=2,
    IamRoles=['arn:aws:iam::129012:role/MyRedshiftRole']
)

print(response)
```



