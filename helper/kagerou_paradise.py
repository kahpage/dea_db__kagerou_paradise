# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== kagerou_paradise1 ====
    if i not in disabled_events:
        event_name = f"kagerou_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            Medium(
                "01_banner.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20150228100703/http://ttc.ninja-web.net/kage-para/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20150228100703/http://ttc.ninja-web.net/kage-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["カゲロウパラダイス", "Kagerou Paradise", "カゲパラ", "kage-para"],
            dates="2015.10.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20150228100703/http://ttc.ninja-web.net/kage-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: dead and unarchived: http://ttc.ninja-web.net/kage-para/kagepara_list.htm (referenced here https://ttc.ninja-web.net/vo-para/vo-para10_list.htm)",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.11.15",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== kagerou_paradise2 ====
    if i not in disabled_events:
        event_name = f"kagerou_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_kage-para02.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20161226045342/http://ttc.ninja-web.net/kage-para/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="カゲロウパラダイス２チラシ絵：いちっちこ様（スイミー）",
            ),
            Medium(
                "02_161002_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20160903111017/http://ttc.ninja-web.net/kage-para/kage-para02_list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20161226045342/http://ttc.ninja-web.net/kage-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=[
                "カゲロウパラダイス2",
                "Kagerou Paradise 2",
                "カゲパラ2",
                "kage-para 2",
            ],
            dates="2016.10.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20161226045342/http://ttc.ninja-web.net/kage-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20160903111017/http://ttc.ninja-web.net/kage-para/kage-para02_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.11.15",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== kagerou_paradise3 ====
    if i not in disabled_events:
        event_name = f"kagerou_paradise{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_kage-para03.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20180901185208/http://ttc.ninja-web.net/kage-para/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="カゲロウパラダイス３チラシ絵：ひなまめ様（Hinageshi）",
            ),
            Medium(
                "03_171015_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20170912233619/http://ttc.ninja-web.net/kage-para/kage-para03_list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20180901185208/http://ttc.ninja-web.net/kage-para/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=[
                "カゲロウパラダイス3",
                "Kagerou Paradise 3",
                "カゲパラ3",
                "kage-para 3",
            ],
            dates="2017.10.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20180901185208/http://ttc.ninja-web.net/kage-para/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20170912233619/http://ttc.ninja-web.net/kage-para/kage-para03_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.11.15",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== kagerou_paradise ====
    # if i not in disabled_events:
    #     event_name = f"kagerou_paradise{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #     #     Location(
    #     #         coordinates=(35.1313699, 136.8980176),
    #     #         address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
    #     #         description="名古屋国際会議場 白鳥ホール",
    #     #         sources=[
    #     #             Source(
    #     #                 "https://web.archive.org/web/20150228100703/http://ttc.ninja-web.net/kage-para/",
    #     #                 (ReliabilityTypes.Reliable, OriginTypes.Official),
    #     #             )
    #     #         ],
    #     #         # comments=None,
    #     #         imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
    #     #         url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
    #     #     ),
    #     ]
    #     event = Event(
    #         aliases=["カゲロウパラダイス", "Kagerou Paradise", "カゲパラ", "kage-para"],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="2026.11.15",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "http://ttc.ninja-web.net/kage-para/",
    ]

    event_group = EventGroup(
        aliases=["カゲロウパラダイス", "Kagerou Paradise", "カゲパラ", "kage-para"],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias "Kagerou Paradise": Guess transliteration from kana',
                (RT.Guess, OT.Unsourced),
            ),
            Source(
                'Alias "kage-para": transliteration from "カゲパラ", syntax to match official "vo-para"',
                (RT.Guess, OT.Unsourced),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.11.15",
    )

    # Check for missing media files and unreferenced media files
    media = [m for e in event_group.events for m in e.media or []] + (
        event_group.media or []
    )
    for m in media:
        if m.path.startswith(("http://", "https://")):
            continue
        p = PATH_MEDIA / m.path
        if not p.exists():
            print(f"Warning: Medium file not found: {p}")

    referenced = {m.path for m in media}
    for p in PATH_MEDIA.rglob("*"):
        if p.is_file() and p.relative_to(PATH_MEDIA).as_posix() not in referenced:
            print(f"Warning: Media file not referenced in event group: {p}")

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
