# Pell Configuration Specification

## Overview

This file will describe the specification of the Pell config files, going into detail how both the json and rc files will function.

Please Note: This file nor the spec is incomplete an should be expected to change at any time through Pell's development.

## Introduction

Pell will use two configuration files:

* `pell.conf` - A json file that will store settings in various sections.
* `.pellrc` - An executable python file that will be loaded and executed similar to how `.bashrc` works with Bash.

There are several things to note here with both files:

* One or both files are optional - That is, the json config can be used without the rc file and vice-versa.
* In the event both files are used - 
    * The json config is loaded before the rc.
    * The rc can override settings in the json file.

## Rationale

The reasoning to use two config files can be narrowed down to four reasons: Speed, Ease of use, Safety and Extensibility.

#### Speed:

As Python code needs to be interpreted, compiled to bytecode, and executed, it will take longer for Pell to start with an rc file then it would with just a json config. Therefore if a fast startup is desired, the json config is a preferred option.

#### Ease of use:

Some users may find a simple json config easier to read than an rc file as it provides a structured list of what settings exist and what they do.

#### Safety:

Unlike the rc file, the json config is not executed and as a result poses very little security risk. Some users may find this desirable as malicious or buggy code could be injected into the rc file which would then be executed by Pell.

*Note: In the future it may be possible for Pell to be set to completely ignore executable functions in the rc file and instead only modify variables should the user choose to do so.*

#### Extensibility:

Given that Pell's rc file is of course executable, it gives the user far greater customisation than what can be offered by the json config. When Pell's plugin system is implemented, the rc file will become an excellent tool for a dynamic Pell configuration.

## Specification Details

The following lists the acceptable variables and settings available to the json config and Python based rc file.

#### JSON `pell.conf`:

The current list of settings is as follows: 

Editor's Note: please feel free to add and change things around. You can find a markdown table generator [here](http://www.tablesgenerator.com/markdown_tables)

An example config can also be found in [Pell/exampleconf/.pell.conf](Pell/exampleconf/.pell.conf)

*Note: Categories (such as theme, core, plugins) are not implemented yet as I need to make changes to how the config loader fetches settings*

##### [`theme`]

| Name     | Description                                                      | Type   | Default        |
|----------|------------------------------------------------------------------|--------|----------------|
| `prompt` | The text that is displayed when the prompt is waiting for input. | string | "pell {0} {1}" |

#### Python `.pellrc`:

This will be updated as the list and format is finalised.
