# Primary Simulator

A simulation tool designed to model a fictional U.S. presidential primary campaign, with a focus on Congressional District-level delegate math and narrative plausibility. This project is part of the worldbuidling process for a speculative fiction series, allowing for dynamic candidate support, delegate allocation, and campaign events.

## Goals

- Simulate Democratic primary elections at the Congressional District level
- Accurately allocate delegates using DNC rules (15% viability threshold, proportional allocation)
- Track candidate support, momentum, and delegate totals
- Support narrative development and in-world content creation

## Current Status

> 🧱 Project structure scaffolding complete  
> 🚧 MVP development in progress — currently building `Candidate` and `CongressionalDistrict` classes

## Project Structure

- `simulator/`: Core logic modules (candidates, districts, allocation engine)
- `data/`: Sample input data (district definitions, voter demographics)
- `scripts/`: CLI or runner scripts
- `tests/`: Unit tests
- `.gitignore`: Keeps virtualenvs, logs, cache, and IDE files out of Git

## Planned Features

- Momentum shifts via events (debates, scandals, endorsements)
- Campaign finance modeling and fundraising feedback loops
- Polling and weekly state-by-state simulation
- Exportable in-world content (e.g. campaign memos, media analysis)

## Getting Started

To initialize your local development environment:

```bash
git clone https://github.com/your-username/primary-simulator.git
cd primary-simulator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # (when dependencies are added)
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

See [LICENSE](LICENSE) for full terms.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

See [LICENSE](LICENSE) for full terms.

## Contributing

This project is currently under solo development and is not accepting outside contributions at this time.

If you're interested in the project or have suggestions, feel free to open an issue or contact the author directly.

A full CONTRIBUTING guide may be added in the future.

## Contact

For questions, feedback, or collaboration inquiries, please reach out to the project author through the GitHub at [github.com/nmiller2379](https://github.com/nmiller2379)
