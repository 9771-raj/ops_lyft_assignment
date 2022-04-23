import boto3
import secret_key


client=boto3.client("ec2","us-west-2",aws_access_key_id=secret_key.aws_access_key_id,
                    aws_secret_access_key=secret_key.aws_secret_access_key)

def delete_instances(instance_ids):
    ec2 = boto3.resource('ec2',"us-west-2",aws_access_key_id=secret_key.aws_access_key_id,
                    aws_secret_access_key=secret_key.aws_secret_access_key)

    ec2.instances.filter(InstanceIds=instance_ids).terminate()


def send_email(temp):
    print(temp)
    sender="gksagar260@gmail.com"
    clie = boto3.client('ses',"us-west-2",aws_access_key_id=secret_key.aws_access_key_id,
                    aws_secret_access_key=secret_key.aws_secret_access_key)

    clie.send_email(
        Destination={
            'ToAddresses': [
                temp
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'Update your environment and name!',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Update your Instances',
            },
        },
        Source=sender,
    )


def checking_tags(tags):
    email_id=""
    environment=""
    name=""
    for tag in tags:
        if tag['Key']=='createdBy':
            email_id+=tag['Value']
            break
    for tag in tags:
        if tag['Key']=='Environment':
            environment=tag['Value']
            break
    for tag in tags:
        if tag['Key']=='Name':
            name=tag['Value']
            break

    # send email
    send_email(email_id)


# for checking all instances and sen mail to respective instances
def solution():
    resources=client.describe_instances()
    for r in resources["Reservations"]:
        for i in r["Instances"]:
            tags=i["Tags"]
            checking_tags(tags)

solution()

