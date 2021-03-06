# Aries Basic Controller Python

A simple pip installable package for controlling aries agents through admin API calls.

# Install

Package only available on the test at the moment.

`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps aries_basic_controller`


# Demo

With docker installed, run the example using ./manage start

This spins up an aries agent and a notebook for both Alice and Bob. Additionally a local von-network is initialised.

To view the tutorials navigate to:
* [Alice notebook](http://localhost:8888) - this contains the majority of the tutorials
* [Bob notebook](http://localhost:8888) - Bob plays the other half of the protocols when needed.

Both notebooks require a token that can be found in the logs. Fetch the logs for the relevant container using these commands:
* docker logs aries-basic-controller-python_alice-notebook_1
* docker logs aries-basic-controller-python_bob-notebook_1




# Sequence Diagram

Built using [Sequence Diagram](https://sequencediagram.org)

![Sequence Diagram](./sequence_diagrams/controller_basic_messaging.svg)

# Contributing

This is a part of a project being developed within the [Open Mined](https://openmined.org) open source community. We welcome new contributors, either join our slack channel or just comment on an issue.
