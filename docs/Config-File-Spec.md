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

Some users may find either a simple json config easier to read than

!! NOT COMPLETE !!
