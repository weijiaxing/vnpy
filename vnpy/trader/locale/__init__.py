import gettext
import json
from pathlib import Path


def _get_trader_dir(temp_name: str) -> Path:
    """
    Get path where trader is running in.
    """
    cwd: Path = Path.cwd()
    temp_path: Path = cwd.joinpath(temp_name)

    if temp_path.exists():
        return temp_path

    home_path: Path = Path.home()
    temp_path = home_path.joinpath(temp_name)

    if not temp_path.exists():
        temp_path.mkdir()

    return temp_path


# Get trader path and load setting
temp_path: Path = _get_trader_dir(".vntrader")
setting_filename: Path = temp_path.joinpath("vt_setting.json")

language: str = ""
if setting_filename.exists():
    try:
        with open(setting_filename, encoding="UTF-8") as f:
            setting: dict = json.load(f)
            language = setting.get("language", "")
    except Exception:
        pass

# Initialize translation
localedir: Path = Path(__file__).parent


if language == "zh_CN":
    translations: gettext.GNUTranslations | gettext.NullTranslations = gettext.NullTranslations()
elif language == "en":
    translations = gettext.translation("vnpy", localedir=localedir, languages=["en"], fallback=True)
else:
    translations = gettext.translation("vnpy", localedir=localedir, fallback=True)

_ = translations.gettext
