#!/usr/bin/env python3
"""Unpack a complete Android source archive, with or without a wrapper folder."""
from pathlib import Path
import shutil
import tempfile
import zipfile


def unpack(archive: Path, destination: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="wtt-source-") as temporary:
        staging = Path(temporary)
        with zipfile.ZipFile(archive) as source:
            for entry in source.infolist():
                name = Path(entry.filename)
                if name.is_absolute() or ".." in name.parts:
                    raise ValueError(f"Unsafe archive entry: {entry.filename}")
            source.extractall(staging)
        projects = [
            item.parent for item in staging.rglob("settings.gradle.kts")
            if (item.parent / "app/build.gradle.kts").is_file()
        ]
        if len(projects) != 1:
            raise ValueError(f"Expected one Android project, found {len(projects)}")
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(projects[0], destination)
        print(f"Complete Android source unpacked to {destination}; no legacy patches applied.")


if __name__ == "__main__":
    unpack(Path("walk-travel-timege-source.zip"), Path("android-src"))
