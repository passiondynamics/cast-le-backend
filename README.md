# cast-le

## Contributing

### Download

```bash
$ git clone git@github.com:passiondynamics/cast-le.git
$ cd cast-le/
```

### Virtual environment

Entering(/creating) the virtual env:
```bash
$ pipenv shell
```

Installing dependencies:
```bash
$ pipenv sync --dev
```

Add a new dependency:
```bash
$ pipenv install {package}
```

### Unit tests

(make sure you're in the virtual env)

Only run unit tests themselves:
```bash
$ pytest tests/unit
```

Run unit tests with coverage information:
```bash
$ pytest --cov=src tests/unit
```

### Integration tests
