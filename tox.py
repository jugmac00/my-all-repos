import argparse
import subprocess
from pathlib import Path
from typing import Optional
from typing import Sequence

from all_repos import cli
from all_repos.config import load_config


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description='Run tox4 on all cloned repositories.',
        usage='python tox.py -C configfile',
    )
    cli.add_common_args(parser)
    cli.add_output_paths_arg(parser)
    args = parser.parse_args(argv)

    config = load_config(args.config_filename)
    results = {"notox": [],
               "successful": [],
               "problems": [],
    }

    repos = list(config.get_cloned_repos())

    for cnt, repo in enumerate(repos, 1):
        if repo == "zopefoundation/zopetoolkit":  # causes buildout/setuptools endless loop
            continue
        if repo == "plone/plone.memoize":  # causes buildout/setuptools endless loop
            continue
        path_tox = Path(config.output_dir, repo, "tox.ini")
        if path_tox.exists():
            print(f"about to run tox for {repo}, {cnt} of {len(repos)}")
            run = subprocess.run(["tox4", "-e py38", "-c", str(path_tox)], stdout=subprocess.DEVNULL)
            if run.returncode == 0:
                print(f"tox4 run successful for {repo}")
                results["successful"].append(repo)
            else:
                print(f"tox4 run failed for {repo}")
                results["problems"].append(repo)

        else:
            print(f"{repo} does not contain a tox configuration. Boo!")
            results["notox"].append(repo)
    
    print(f'notox: {len(results["notox"])}')
    print(f'{results["notox"]}')
    print(f'successful: {len(results["successful"])}')
    print(f'{results["successful"]}')
    print(f'problems: {len(results["problems"])}')
    print(f'{results["problems"]}')
    return 0


if __name__ == '__main__':
    exit(main())
