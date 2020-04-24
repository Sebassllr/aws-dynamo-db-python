import boto3

'''
- Copy from one table to another 

'''
client = boto3.client('dynamodb')

src_table = input("Enter source table: ")
dest_table = input("Enter destination table: ")

resource = boto3.resource("dynamodb")
src_table_content = resource.Table(src_table).scan()
src_table_content_items = src_table_content['Items']

dest_table_content = resource.Table(dest_table)

print("Copying data from " + src_table + " to " + dest_table)
for item in src_table_content_items:
    dest_table_content.put_item(Item=item)

print("Process Completed :) ")
