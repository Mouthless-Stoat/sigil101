# Basic of Json

`[] json` is the main language that ruleset are written in, it is not a very complicated language it can only carry hard-coded data and can't really do anything else. `[] json` are written similarly to `Dictionary`. Let look at a example `[] json` file:

@f test.json

```json
{
    "string": "TEST",
    "array": [1, 2, 3]
}
```

First, everything must be between `{}` and every key have to be a `String` unlike with `Dictionary`, other than that they are pretty similar. There is a few quirk with json thought, most notable is you can't have trailing or hanging comma.
