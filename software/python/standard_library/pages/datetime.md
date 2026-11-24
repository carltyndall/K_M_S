# datetime

`datetime` provides dates, times, durations, and time-zone-aware timestamps. Use aware UTC values for unambiguous instants; naive values have no attached time zone.

```python
from datetime import date, datetime, timedelta, timezone

day = date.fromisoformat('2024-02-28')
print(day + timedelta(days=1))  # 2024-02-29
instant = datetime(2024, 2, 29, 12, 0, tzinfo=timezone.utc)
print(instant.isoformat())  # 2024-02-29T12:00:00+00:00
print(datetime.fromisoformat('2024-02-29T12:00:00+00:00') == instant)  # True
```

For regional time zones and daylight-saving transitions, use `zoneinfo.ZoneInfo` rather than a fixed UTC offset. Comparing naive and aware datetimes for ordering raises `TypeError`. Formatting with `strftime()` and parsing with `strptime()` use format directives; see the [format-code reference](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes). See also [comparisons](../../built_in_types/pages/comparisons.md).

[Python documentation](https://docs.python.org/3/library/datetime.html)