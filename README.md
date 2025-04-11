# ivbf

IVBF (Ionvop's Brainfuck) is a custom interpreted language inspired by Brainfuck.

## Syntax

`+;` Increment the current cell by 1.

- `+<value>;` Increment the current cell by value.

- `+<address>:<value>;` Increment the cell at address by value.

`-;` Decrement the current cell by 1.

- `-<value>;` Decrement the current cell by value.

- `-<address>:<value>;` Decrement the cell at address by value.

`*;` Multiply the current cell by 2.

- `*<value>;` Multiply the current cell by value.

- `*<address>:<value>;` Multiply the cell at address by value.

`/;` Divide the current cell by 2.

- `/<value>;` Divide the current cell by value.

- `/<address>:<value>;` Divide the cell at address by value.

`%;` Modulo the current cell by 2.

- `%<value>;` Modulo the current cell by value.

- `%<address>:<value>;` Modulo the cell at address by value.

`=;` Set the current cell to 0.

- `=<value>;` Set the current cell to value.

- `=<address>:<value>;` Set the cell at address to value.

`>;` Increment the pointer by 1.

- `><value>;` Increment the pointer by value.

- `><address>:<value>;` Set the pointer to address and offset by value.

`.;` Print the current cell as an ASCII character.

- `.<value>;` Print the next number of cells as ASCII characters starting from the current cell.

- `.<address>:<value>;` Print the next number of cells as ASCII characters starting from address.

`&;` Copy the current cell to the next cell.

- `&<value>;` Copy the current cell to a cell offset from the current cell by value.

- `&<address>:<value>;` Copy the current cell to the cell at address and the next number of cells.

`#;` Print the current cell as a number.

- `#<value>;` Print the next number of cells as numbers starting from the current cell.

- `#<address>:<value>;` Print the next number of cells as numbers starting from address.

`?<label>;` Jump to a label.

- `?<operator><value>:<label>;` Jump to a label if the operator is true.

- `?<operator><value>:<label>:<else>;` Jump to a label if the operator is true, otherwise jump to else.

`!<label>;` A label to jump to.

`<;` Return to the last jump call stack.

`~<string>;` Store a string with one ASCII value for each of the next cells starting from the current cell.

## Examples

### Hello World

```
~Hello, world!;.13;
```

`~Hello, world!` stores the string "Hello, world!" for each subsequent cells starting from the current cell.

`.13;` Prints the next 13 cells as ASCII characters starting from the current cell.

### Fizzbuzz

```
~fizzbuzz\n;

!start;>10:0;+;?>100:end;&;>;
%15;?=0:fb;>-1;&;>;
%3;?=0:f;>-1;&;>;
%5;?=0:b;>-1;#;.8:1;?start;

!f;.0:4;.8:1;?start;
!b;.4:4;.8:1;?start;
!fb;.0:9;?start;

!end;
```

`~fizzbuzz\n;` stores the string "fizzbuzz\n" for each subsequent cells starting from the current cell.

`!start;` A label named `start`.

`>10:0;` Set the pointer to cell 10 and offset by 0.

`+;` Increment the current cell by 1.

`?>100:end;` Jump to the label `end` if the current cell is greater than 100.

`&;` Copy the current cell to the next cell.

`>;` Increment the pointer by 1.

`%15;` Modulo the current cell by 15.

`?=0:fb;` Jump to the label `fb` if the current cell is equal to 0.

`>-1;` Move the pointer back 1 cell.

`%3;` Modulo the current cell by 3.

`?=0:f;` Jump to the label `f` if the current cell is equal to 0.

`%5;` Modulo the current cell by 5.

`?=0:b;` Jump to the label `b` if the current cell is equal to 0.

`#;` Print the current cell as a number.

`.8:1;` Prints the next 1 cell as ASCII characters starting from cell 8.

`?start;` Jumps to the label `start`.

`!f;` A label named `f`.

`.0:4;` Prints the next 4 cells as ASCII characters starting from cell 0.

`!b;` A label named `b`.

`.4:4;` Prints the next 4 cells as ASCII characters starting from cell 4.

`!fb` A label named `fb`.

`.0:9;` Prints the next 9 cells as ASCII characters starting from cell 0.

`!end;` A label named `end`.