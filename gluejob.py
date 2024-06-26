pip install boto3
import boto3
# Initialize a session using AWS Glue
client = boto3.client('glue', region_name='us-west-2')

# Create Glue Job
response = client.create_job(
    Name='my-glue-job',
    Role='AWSGlueServiceRole',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://my-script-bucket/scripts/glue-etl-script.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--TempDir': 's3://my-temp-bucket/temp/',
        '--job-bookmark-option': 'job-bookmark-enable'
    },
    MaxRetries=0,
    Timeout=2880
)

print(response)
