# Contract for: List All lifts

- **Route**: `/`
- **Params**: none
- **Method**: `GET`

### Description

- This Route returns an object with all the lifts and their details.(state)
- Any Parameter Passed to this route via queryparams will be ignored

**Response schema**

```
{
    id:{
        id: id of the lift,
        current_floor: Current floor on which the lift is,
        move_up: A boolean value when false means lift moved down,
        busy: A boolean value when true means lift is in use,
        is_OOO: A boolean field marks lifts under maintenance and active,
        door_open: A boolean value that indicates the state of door
    },
}
```

### Image gallery

![image](https://user-images.githubusercontent.com/57758447/221545753-66dab1d8-16b6-4ede-8858-9646a59c7e47.png)
