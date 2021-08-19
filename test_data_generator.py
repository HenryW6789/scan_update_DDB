import boto3
import datetime
import time
start_time = time.time()

def add_testing_items(amount):
# add items
    i = 1
    while i<=amount:
        response = table.put_item(
            Item={
                    'id': str(i),
                    'created': str(datetime.datetime.now())
                    }
            )
        # print (response)
        i += 1
        print (i)

if __name__ == '__main__':
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object
    table = dynamodb.Table('stuff')

    # Print out some data about the table.
    print(table.creation_date_time)
    # add_items()
    add_testing_items(5000)

    print(table.item_count)

    print ("Completed!")
    print("--- %s seconds ---" % (time.time() - start_time))

    # Adding 5000 items spends 435 seconds with CapacityUnits: 10
    # Adding 5000 items spends 252 seconds with CapacityUnits: 50