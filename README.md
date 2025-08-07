# Calculator v2.0

A terminal-based scientific calculator supporting basic arithmetic, roots, logarithms, and trigonometric operations. The calculator provides an interactive loop and a simple menu system for repeated calculations, help, and history viewing.

---

## Features

- Basic arithmetic: `+`, `-`, `*`, `/`, `**`
- Root extraction: `root <number> <degree>`
- Logarithms: `log <number> <base>`
- Trigonometry: `sin`, `cos`, `tan`, `cot`
- Input validation and error handling (e.g., division by zero, invalid log/root inputs)
- Operation history tracking
- Interactive menu system

---

## Usage

Run the script and follow the terminal prompts.

### Input Formats

| Operation   | Symbol  | Format Example       |
|-------------|---------|----------------------|
| Add         | `+`     | `3 + 5`              |
| Subtract    | `-`     | `10 - 2`             |
| Multiply    | `*`     | `4 * 7`              |
| Divide      | `/`     | `20 / 4`             |
| Power       | `**`    | `2 ** 3`             |
| Root        | `root`  | `root 27 3`          |
| Logarithm   | `log`   | `log 100 10`         |
| Sine        | `sin`   | `sin 1.57`           |
| Cosine      | `cos`   | `cos 0.5`            |
| Tangent     | `tan`   | `tan 0.78`           |
| Cotangent   | `cot`   | `cot 1`              |

*Note: All inputs must be space-separated.*

---

## Menu Options

After each calculation, choose from:

- **1** — New Calculation
- **2** — Menu:
  - **1** New Calculation
  - **2** Show History
  - **3** Help
  - **4** Exit
- **3** — Exit Program

---

## Requirements

- Python 3.x
- No external dependencies (only uses built-in `math` module)

---

## License

This project is licensed under the MIT License.