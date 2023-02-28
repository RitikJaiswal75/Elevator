# Contract for: Move Lift

- **Route**: `create/`
- **Params**: `floor=<number>`
- **Method**: `GET`

### Description

- This Route moves closest lift to the desired floor
- This Route accepts a query param of floor having an integer value.
- If no Parameter is passed it calls a lift to first floor.

**Response schema**
```
{
    Lift moved: {
        id: id of the lift moved,
        current_floor: Current floor on which the lift is (after moving),
        move_up: A boolean value when false means lift moved down,
        busy: A boolean value when true means lift is in use,
        is_OOO: A boolean field marks lifts under maintenance and active,
        door_open: A boolean value that indicates the state of door
    }
}
```

### Image gallery
- ![image](https://user-images.githubusercontent.com/57758447/221764670-7339ed9a-d9cf-4a0d-a22a-7cc241cee0af.png)
