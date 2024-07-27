
# AWS SES daily utilisation alert using Lambda

In order to efficiently manage SES usage and ensure it stays within the allocated limits, 
This Python function that will run on Lambda and fetch data through API calls that are made on the AWS SES service and sending alerts on the SNS topic registered if utilisation go above a certain threshold.



## Screenshots
Below is the fuction overview -

![App Screenshot](https://i.postimg.cc/4yq5KftN/Screenshot-from-2024-03-12-09-28-14.png)

Here are the polices that is assigned to Lambda fuction - 

Note: Full Access polices are given in Test enviorment, As per AWS Polices try to give minimal access.

![App Screenshot](https://i.postimg.cc/qvjhzwWD/Screenshot-from-2024-03-12-09-34-43.png)
