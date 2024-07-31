import subprocess


def get_current_version():
    result = subprocess.run(
        [
            'git',
            'describe',
            '--tags',
            '--abbrev=0',
        ],
        stdout=subprocess.PIPE,
        text=True)
    return result.stdout.strip()


def increment_version(version):
    major, minor, patch = map(
        int,
        version.lstrip('v').split('.'),
    )
    patch += 1
    return f'v{major}.{minor}.{patch}'


def main():
    current_version = get_current_version()
    new_version = increment_version(current_version)
    subprocess.run([
        'git',
        'tag',
        new_version,
    ])
    subprocess.run([
        'git',
        'push',
        '--tags',
    ])


if __name__ == "__main__":
    main()
