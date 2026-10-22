"""An optional local timing exercise, not evidence of scientific parity."""

import json
import platform
from timeit import repeat

from pyrverse_port import center

if __name__ == "__main__":
    values = tuple(float(index) for index in range(1_000))
    repetitions = 1_000
    samples = repeat(lambda: center(values), number=repetitions, repeat=5)
    print(
        json.dumps(
            {
                "example": "center",
                "python": platform.python_version(),
                "platform": platform.platform(),
                "input_size": len(values),
                "calls_per_repeat": repetitions,
                "seconds_per_call": [sample / repetitions for sample in samples],
                "note": "Local timing only; no upstream comparison or speed claim.",
            },
            indent=2,
        )
    )
