# Contract for: Create Lifts

- **Route**: `create/`
- **Params**: `count=<number>`
- **Method**: `GET`

### Description

- This Route creates multiple lifts when called.
- This Route accepts a query param of count having an integer value.
- If no Parameter is passed it creates 0 lifts.

**Response schema**

```
{
    status: its a string message thats says lift created,
    count: count of the lifts created,
}
```

### Image gallery
- ![image](https://user-images.githubusercontent.com/57758447/221763498-3c2937fe-4773-4221-b416-6c16347d1e45.png)
