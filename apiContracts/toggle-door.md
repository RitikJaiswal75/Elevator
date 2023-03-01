# Contract for: Marking a lift OOO

- **Route**: `door/`
- **Params**: `lift=<lift_number>`
- **Method**: `GET`

### Description

- This api changes the property of door_open for specified lift.
- you can specify the lift by passing in a query parameter of lift
- In case you enter the number mort than the count of lifts available api returns a message of lift not found

**Response Schema**

- Success

```
{
    id: id of the lift moved,
    current_floor: Current floor on which the lift is (after moving),
    move_up: A boolean value when false means lift moved down,
    busy: A boolean value when true means lift is in use,
    is_OOO: A boolean field marks lifts under maintenance and active,
    door_open: A boolean value that indicates the state of door,
}
```

- Failure

```
{
    "Message": "Lift does not exist"
}
```

### Image gallery

- Success

  - ![image](https://user-images.githubusercontent.com/57758447/221789563-bf868040-ac94-46f8-b655-c4b3b391fb46.png)
  - ![image](https://user-images.githubusercontent.com/57758447/221789613-75648f5c-88e8-434a-abba-3ba3d00f1bcc.png)

- Failure
  - ![image](https://user-images.githubusercontent.com/57758447/221789534-262aae70-dd92-4c82-a4ae-4b9d8a968600.png)
