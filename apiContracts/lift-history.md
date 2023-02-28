# Contract for: Marking a lift OOO

- **Route**: `history/`
- **Params**: `lift=<lift_number>`
- **Method**: `GET`

### Description

- This API gets all the user interaction for the specified lift
- You can specify the lift number by passing the query parameter of lift
- In case there is no parameter specified the api returns the history of the first lift
- The api will return an error if the number for lift parameter exceeds the count of lifts present.

**Response Schema**

- Success
```
{
    "Lift id": Id of the selected lift,
    "history" : [] list of user interactions in the form of string
}
```

- Failure
```
{
    "Message":"Lift not Found",
}
```

### Image gallery

- Success
  - 

- Failure
  - 