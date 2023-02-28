# Contract for: Marking a lift OOO

- **Route**: `ooo/`
- **Params**: `lift=<lift_number>`
- **Method**: `GET`

### Description

- This Route marks the desired lift out of order
- when this api is called again with same number it marks the lift active.
- This Route accepts a query param of lift having an integer value.
    - (the lift_number here is not the id of the lift its similar to shutting down the third lift)
- If no parameter is passed, a response of lift does not exist is generated

**Response schema**

- Success
```
{
    message: lift marked active/ooo
}
```

- Failure
```
{
    message: Lift does not exist
}
```

### Image gallery

- Success
  - ![image](https://user-images.githubusercontent.com/57758447/221781037-0a267094-07aa-44e2-9caa-0c78e0278f57.png)

- Failure
  - ![image](https://user-images.githubusercontent.com/57758447/221780971-170b6d76-f96b-4d01-a397-4bdee2fcb37f.png)
