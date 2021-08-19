import boto3
import time
start_time = time.time()

def scan_table():
    print ("table scanning...")
    return table.scan()

def update_item(my_item):
    print ("updating the item:", my_item)
    return table.update_item(
        Key = {
            "id": my_item['id'],
            "created": my_item['created']
        },
        UpdateExpression = "set test =:t",
        ExpressionAttributeValues = {
            ':t': 1
        },
        ReturnValues="UPDATED_NEW"
    )

def has_test_attribute(my_item):
    if 'test' in my_item:
        return True
    else:
        return False
    

if __name__ == '__main__':
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object
    table = dynamodb.Table('stuff')

    # counting records
    scan_results = scan_table()
    print (scan_results['Count'])

    # loop for updating the items which doesn’t already have the value set.
    for item in scan_results['Items']:
        if has_test_attribute(item):
            # print ("'test' is already in id: ", item['id'])
            pass
        else:
            # print ("'test' is NOT in id: ", item['id'])
            update_item(item)
   
    # example: {'id': '228', 'created': '2021-08-18 12:06:35.022963'}

    print ("Completed!")
    print("--- %s seconds ---" % (time.time() - start_time))

    # 180s for updating 1000 items with CapacityUnits: 5
    # updating 5000 items spends 478 seconds with CapacityUnits: 10
    # updating 5000 items spends 948? seconds with CapacityUnits: 50