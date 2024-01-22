env=input("enter the cloud platform:")

if env == "aws" or env == "AWS":
    print("You are in AWS environment")
elif env == "azure" or env == "AZURE":
    print("You are in Azure environment")
elif env == "gcp" or env == "GCP":
    print("You are in GCP environment")
else:
    print ("you are in not in aws. Your are in another environment ")
