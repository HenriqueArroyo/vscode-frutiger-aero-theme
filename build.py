#!/usr/bin/env python3
"""Build do Frutiger Aero Glass.

    python3 build.py            # gera temas, ícones, SVG, CSS e relatório de contraste
    python3 build.py --vsix     # idem + empacota dist/<nome>-<versão>.vsix

Não depende de Node: o .vsix é montado direto com zipfile.
"""

import json
import sys
import base64
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from background import build_svg  # noqa: E402
from icons import icon_theme, render_icons  # noqa: E402
from palettes import VARIANTS  # noqa: E402
from tokens import semantic_token_colors, token_colors  # noqa: E402
from workbench import workbench_colors  # noqa: E402

THEMES_DIR = ROOT / "themes"
DIST_DIR = ROOT / "dist"
ASSETS_DIR = ROOT / "assets"
ICONS_DIR = ROOT / "icons"
ICON_THEME = "aeroglass-icon-theme.json"

SEL_ALL = '.monaco-workbench:is([class*="aeroglass-dark"],[class*="aeroglass-light"])'
SEL_DARK = '.monaco-workbench[class*="aeroglass-dark"]'
SEL_LIGHT = '.monaco-workbench[class*="aeroglass-light"]'


# ---------------------------------------------------------------- contraste --
def _luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")[:6]
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(fg: str, bg: str) -> float:
    l1, l2 = sorted((_luminance(fg), _luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


CHECKS = [
    # (papel do texto, papel do fundo, mínimo)
    *[(r, "bg", 4.5) for r in (
        "fg", "comment", "keyword", "string", "escape", "regex", "number", "constant", "type",
        "function", "variable", "parameter", "property", "operator", "punctuation", "tag",
        "attribute", "heading", "link", "invalid")],
    ("fgMuted", "bgAlt", 4.5),
    ("fg", "bgAlt", 4.5),
    ("tabActiveFg", "tabActiveBg", 4.5),
    ("tabInactiveFg", "tabInactiveBg", 4.5),
    ("headerFg", "headerBg", 4.5),
    ("statusFg", "statusBg", 4.5),
    ("buttonFg", "button", 4.5),
    ("titleFg", "titleBg", 4.5),
    ("activityFg", "activityBg", 3.0),   # ícones: componente não textual
]


def contrast_report(name: str, p: dict) -> int:
    failures = 0
    print(f"\n  Contraste: {name}")
    for fg_role, bg_role, minimum in CHECKS:
        ratio = contrast(p[fg_role], p[bg_role])
        ok = ratio >= minimum
        failures += not ok
        mark = "ok " if ok else "FALHA"
        print(f"    [{mark}] {fg_role:<14} sobre {bg_role:<14} {ratio:5.2f}:1 (mín {minimum})")
    return failures


# --------------------------------------------------------------------- temas --
def build_themes() -> int:
    THEMES_DIR.mkdir(exist_ok=True)
    failures = 0
    for filename, palette in VARIANTS.items():
        theme = {
            "$schema": "vscode://schemas/color-theme",
            "name": palette["name"],
            "type": palette["kind"],
            "semanticHighlighting": True,
            "colors": workbench_colors(palette),
            "tokenColors": token_colors(palette),
            "semanticTokenColors": semantic_token_colors(palette),
        }
        (THEMES_DIR / filename).write_text(json.dumps(theme, indent=2, ensure_ascii=False) + "\n")
        print(f"  tema   -> themes/{filename} ({len(theme['colors'])} cores de interface)")
        failures += contrast_report(palette["name"], palette)
    return failures


# -------------------------------------------------------------------- ícones --
def build_icons() -> None:
    ICONS_DIR.mkdir(exist_ok=True)
    for old in ICONS_DIR.glob("*.svg"):  # remove ícones que saíram do catálogo
        old.unlink()
    icons = render_icons()
    for name, svg in icons.items():
        (ICONS_DIR / name).write_text(svg)
    theme = icon_theme()
    (THEMES_DIR / ICON_THEME).write_text(json.dumps(theme, indent=2, ensure_ascii=False) + "\n")
    print(f"  ícones -> icons/ ({len(icons)} SVGs), themes/{ICON_THEME} "
          f"({len(theme['fileExtensions'])} extensões, {len(theme['fileNames'])} nomes, "
          f"{len(theme['folderNames'])} pastas)")


# ----------------------------------------------------------------- glass/css --
def build_glass() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)
    DIST_DIR.mkdir(exist_ok=True)
    svg = build_svg()
    (ASSETS_DIR / "aero-sky.svg").write_text(svg)

    data_uri = "data:image/svg+xml;base64," + base64.b64encode(" ".join(svg.split()).encode()).decode()
    css = (ROOT / "src" / "glass.css").read_text()
    css = (css.replace("$DARK", SEL_DARK)
              .replace("$LIGHT", SEL_LIGHT)
              .replace("$A", SEL_ALL)
              .replace("__SKY__", data_uri))
    header = "/* Gerado por build.py a partir de src/glass.css. Não edite este arquivo. */\n"
    (DIST_DIR / "aero-glass.css").write_text(header + css)
    print(f"  svg    -> assets/aero-sky.svg ({len(svg) // 1024} KB)")
    print(f"  css    -> dist/aero-glass.css ({len(header + css) // 1024} KB, SVG embutido)")


# ---------------------------------------------------------------------- vsix --
CONTENT_TYPES = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension=".json" ContentType="application/json"/>
  <Default Extension=".vsixmanifest" ContentType="text/xml"/>
  <Default Extension=".md" ContentType="text/markdown"/>
  <Default Extension=".png" ContentType="image/png"/>
  <Default Extension=".svg" ContentType="image/svg+xml"/>
</Types>
"""

MANIFEST = """<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="{name}" Version="{version}" Publisher="{publisher}"/>
    <DisplayName>{displayName}</DisplayName>
    <Description xml:space="preserve">{description}</Description>
    <Tags>theme,color-theme,frutiger-aero,aero,glass</Tags>
    <Categories>Themes</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{engine}"/>
      <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value=""/>
      <Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value=""/>
      <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="ui,workspace"/>
      <Property Id="Microsoft.VisualStudio.Code.LocalizedLanguages" Value=""/>
      <Property Id="Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown" Value="true"/>
    </Properties>
    {icon_meta}
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/CHANGELOG.md" Addressable="true"/>
    {icon_asset}
  </Assets>
</PackageManifest>
"""


def build_vsix() -> Path:
    pkg = json.loads((ROOT / "package.json").read_text())
    files = ["package.json", "README.md", "CHANGELOG.md"]
    files += [str(p.relative_to(ROOT)) for p in sorted(THEMES_DIR.glob("*.json"))]
    files += [str(p.relative_to(ROOT)) for p in sorted(ICONS_DIR.glob("*.svg"))]
    icon = pkg.get("icon")
    if icon:
        files.append(icon)

    manifest = MANIFEST.format(
        name=pkg["name"], version=pkg["version"], publisher=pkg["publisher"],
        displayName=pkg["displayName"], description=pkg["description"],
        engine=pkg["engines"]["vscode"],
        icon_meta=f"<Icon>extension/{icon}</Icon>" if icon else "",
        icon_asset=(f'<Asset Type="Microsoft.VisualStudio.Services.Icons.Default" '
                    f'Path="extension/{icon}" Addressable="true"/>') if icon else "",
    )
    out = DIST_DIR / f"{pkg['name']}-{pkg['version']}.vsix"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("extension.vsixmanifest", manifest)
        for f in files:
            z.write(ROOT / f, f"extension/{f}")
    print(f"  vsix   -> {out.relative_to(ROOT)}")
    return out


def main() -> int:
    print("Frutiger Aero Glass: build")
    failures = build_themes()
    build_icons()
    build_glass()
    if "--vsix" in sys.argv:
        build_vsix()
    if failures:
        print(f"\n{failures} verificação(ões) de contraste abaixo do mínimo.")
        return 1
    print("\nContraste: todas as verificações passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
