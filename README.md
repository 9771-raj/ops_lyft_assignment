## ops_lyft_assignment
Tasks:

1. Create an AWS Lambda function which would run every hour and check EC2 instances which don’t have ‘Environment’ and ‘Name’ tags attached on it.
2. It should check the ‘created by’ tag whose value would be an emailId and if it finds an instance which doesn't have the aforementioned tags, it should send them an email to remind them to tag the instance.
3. The email should contain the instance ID and the tag keys it is missing.
4. Once 6 hours have passed after sending the email, it should terminate the instance with an email notifying the user of the same.
