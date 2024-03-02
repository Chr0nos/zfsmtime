#!/usr/bin/python3
import os
import pyinotify
import click
from typing import Never, Generator


def path_iter(root: str, path: str) -> Generator[str, None, None]:
    folder_splited = path.removeprefix(root).split("/")[::-1]
    for i in range(0, len(folder_splited)):
        fullpath = os.path.join(root, *folder_splited[i:][::-1])
        yield fullpath


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, root: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.root = root

    def process_default(self, event: pyinotify.Event) -> None:
        print(event, event.pathname)
        for folder in path_iter(self.root, event.path):
            print("->", folder)
            try:
                os.utime(folder, None)
            except FileNotFoundError:
                pass
            except PermissionError:
                print(f"Permission error on {folder}")


def watch_directory(directory: str) -> Never:
    wm = pyinotify.WatchManager()
    handler = EventHandler(directory)
    notifier = pyinotify.Notifier(wm, handler)
    wm.add_watch(
        directory,
        pyinotify.IN_CLOSE_WRITE
        | pyinotify.IN_CREATE
        | pyinotify.IN_DELETE
        | pyinotify.IN_MOVED_TO
        | pyinotify.IN_MOVED_FROM,
        rec=True,
        auto_add=True,
    )
    print(f"Watching {directory}")
    notifier.loop()


@click.group()
def cli(): ...


@cli.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, dir_okay=True))
def watch(directory: str) -> Never:
    watch_directory(directory)


if __name__ == "__main__":
    cli()
