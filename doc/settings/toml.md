```
# units.toml

[second]
label   = { singular = "second", plural = "seconds" }
aliases = ["s", "sec", "seconds"]

[minute]
label      = { singular = "minute", plural = "minutes" }
aliases    = ["min", "minutes"]
multiplier = 60
to_unit    = "second"

[hour]
label      = { singular = "hour", plural = "hours" }
aliases    = ["h", "hr", "hours"]
multiplier = 60
to_unit    = "minute"

[day]
label      = { singular = "day", plural = "days" }
aliases    = ["d", "days"]
multiplier = 24
to_unit    = "hour"

[year]
label      = { singular = "year", plural = "years" }
aliases    = ["y", "yr", "years", "julian_year", "julian years"]
multiplier = 365.25
to_unit    = "day"
```

