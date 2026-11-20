"""Build the single-file edition from the native Agent Skills sources."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "e-s-v"
GUIDES = (
    ("source-selection", "sources"),
    ("learning-map", "map"),
    ("coverage-delivery", "lessons"),
    ("practice", "practice"),
)
INTRO = """# E.S-V SKILL · 通用单文件

将本文件作为附件、知识文件或对话文字交给智能体，然后说“请按 E.S-V 教我这门课”。若要分次粘贴，先发送全部内容，再发出课程任务。本文件写给授课智能体，课程资料由学习者另行提供或选定。

Attach this file, add it to the agent’s instructions, or paste its text. Then ask “Teach me this course using E.S-V.” Teach in the learner’s language.

"""


def render():
    front, _, body = (SKILL / "SKILL.md").read_text(encoding="utf-8").partition("\n---\n")
    if not front.startswith("---\n") or not body.startswith("\n# E.S-V SKILL\n"):
        raise ValueError("Unexpected SKILL.md front matter or title")
    body = body.removeprefix("\n# E.S-V SKILL\n").strip()
    sections = []
    for filename, anchor in GUIDES:
        link = f"references/{filename}.md"
        if f"]({link})" not in body:
            raise ValueError(f"Missing guide link: {link}")
        body = body.replace(f"]({link})", f"](#{anchor})")
        guide = (SKILL / link).read_text(encoding="utf-8").strip()
        sections.append(f'<a id="{anchor}"></a>\n\n{guide}')
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8").strip()
    return INTRO + "\n\n".join([body, *sections, "## License\n\n" + license_text]) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check that the published edition is current")
    args = parser.parse_args()
    output = ROOT / "E.S-V.portable.md"
    content = render()
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != content:
            raise SystemExit("Rebuild E.S-V.portable.md with this script")
        print("Portable edition matches the native skill and four guides.")
    else:
        output.write_bytes(content.encode("utf-8"))


if __name__ == "__main__":
    main()
