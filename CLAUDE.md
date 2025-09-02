# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Install dependencies**: `poetry install`
- **Run tests**: `pytest`
- **Run linting**: `ruff check` or `ruff check --fix` to auto-fix
- **Format code**: `ruff format`
- **Django management**: `python manage.py <command>` (uses example_project.settings)
- **Database migrations**: `python manage.py migrate`
- **Pre-commit hooks**: `pre-commit run --all-files`

## Architecture

This is a Django package that extends py-moneyed with foreign exchange (FX) rate functionality. The package consists of two main modules:

### Core Components

- **moneyed_fx/**: Main Django app containing FX rate storage and retrieval logic
  - `models.py`: FxRate model stores exchange rates with timestamp and base currency indexing
  - `services.py`: Core FX functions including `get_current_rate()`, `get_stored_rate()`, and `update_all_rates()`
  - `moneyed_patches.py`: Monkey patches py-moneyed's Money class to add `fx_to()` method

- **open_exchange_rates/**: Default exchange rate data source
  - `services.py`: Implements the required interface (`get_current_rates()`, `get_rate_for()`, `use_reverse_rate()`)
  - `api.py`: OpenExchangeRates API client for Latest and Historical endpoints

### Key Design Patterns

- **Pluggable rate sources**: Exchange rate sources are configurable via `MONEYED_FX_RATE_SOURCE` setting
- **Monkey patching**: Adds `fx_to()` method to py-moneyed's Money class without modifying the original library
- **Rate caching**: FX rates are stored in database with daily cronjob updates via `update_all_rates()`
- **Reverse rate handling**: Special logic for currencies like VND that have insufficient decimal precision

### Configuration Requirements

- Must be installed AFTER `hordak` app in Django's `INSTALLED_APPS`
- Requires `CURRENCIES` setting (can be callable or list)
- Needs daily cronjob running `moneyed_fx.services.update_all_rates` at ~4am UTC
- Optional: Set `MONEYED_FX_RATE_SOURCE` to use custom exchange rate provider

### Testing

- Uses pytest-django with `example_project.settings`
- Test database reuse enabled with `--reuse-db --no-migrations`
- Factory Boy for test data generation
- Mock exchange rate source in `tests/mock_source/`
