from pathlib import Path
import os
import tempfile
import json


sources = [
    "https://github.com/hannesdelbeke/plugget-pkgs.git",
]

# paths
TEMP_PLUGGET = Path(tempfile.gettempdir()) / "plugget"
PLUGGET_DIR = Path(os.getenv("APPDATA")) / "plugget"
INSTALLED_DIR = PLUGGET_DIR / "installed"
# PLUGGET_SETTINGS = PLUGGET_DIR / "settings.json"
# todo expose PLUGGET_DIR to env var so it can be changed
INSTALLED_DIR.mkdir(exist_ok=True, parents=True)


# get settings for the actions etc, requires unique name for each action
# todo support duplicates of the same settings for each app (blender, blender2, maya, etc)
# actions request plugget for their settings
# plugget manages & saves the settings and justs returns them

def _settings_name(name):
    return PLUGGET_DIR / f"settings_{name}.json"


def load_settings(name):
    settings_path = _settings_name(name)
    if not settings_path.exists():
        return {}
    try:
        with open(settings_path, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {}


def save_settings(name, settings):
    with open(_settings_name(name), "w") as f:
        json.dump(settings, f, indent=4)
        print("saved settings:", _settings_name(name))


# todo in settings we need a add_repo, remove_repo, list_repos.
# todo cleanup simple way of loading
settings_data = load_settings("plugget")
sources = settings_data.get("sources", sources)
save_settings("plugget", {"sources": sources})
