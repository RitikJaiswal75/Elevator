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
  - ![image](https://user-images.githubusercontent.com/57758447/221785253-f6423272-8c4d-413b-9544-2f393660579a.png)

- Failure
  - ![image](https://user-images.githubusercontent.com/57758447/221785211-d54a5a58-8b4f-48fb-86bd-55e75b0f9fca.png)
