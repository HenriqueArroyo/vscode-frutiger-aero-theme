"""Camada 3: tema de ícones de arquivo "Frutiger Aero Glass Icons".

Gera um SVG por ícone (ladrilhos de vidro com brilho, documentos e pastas
aqua) e o JSON do icon theme. Tudo em viewBox 32x32; o Explorer exibe a 16px.
"""

import html
import math

FONT = "'Segoe UI','Noto Sans','DejaVu Sans',Arial,sans-serif"


# ------------------------------------------------------------------ cores --
def _rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(c1: str, c2: str, t: float) -> str:
    a, b = _rgb(c1), _rgb(c2)
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(a, b))


def light(c: str, t: float) -> str:
    return mix(c, "#FFFFFF", t)


def dark(c: str, t: float) -> str:
    return mix(c, "#000000", t)


# ----------------------------------------------------------------- glifos --
# Desenhados em branco sobre o ladrilho, centrados em (16, 16.5).
def _gear() -> str:
    pts = []
    for i in range(16):
        ang = math.pi * 2 * i / 16
        r = 10 if i % 2 == 0 else 7.6
        pts.append(f"{16 + r * math.cos(ang):.2f},{16.5 + r * math.sin(ang):.2f}")
    return (f'<polygon points="{" ".join(pts)}" fill="#FFF"/>'
            '<circle cx="16" cy="16.5" r="3.4" fill="currentColor"/>')


GLYPHS = {
    "gear": _gear(),
    "database": (
        '<path d="M8 10.5v12c0 2 3.6 3.5 8 3.5s8-1.5 8-3.5v-12" fill="#FFF"/>'
        '<ellipse cx="16" cy="10.5" rx="8" ry="3.3" fill="#FFF"/>'
        '<path d="M8 15c0 2 3.6 3.5 8 3.5s8-1.5 8-3.5M8 19.5c0 2 3.6 3.5 8 3.5s8-1.5 8-3.5" '
        'fill="none" stroke="currentColor" stroke-width="1.4"/>'
    ),
    "terminal": (
        '<path d="M8 11l6 5.5-6 5.5" fill="none" stroke="#FFF" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<rect x="15.5" y="20.5" width="9" height="3" rx="1.5" fill="#FFF"/>'
    ),
    "branch": (
        '<path d="M11 9v14M11 18c0-4 10-2 10-7" fill="none" stroke="#FFF" stroke-width="2.6" stroke-linecap="round"/>'
        '<circle cx="11" cy="9" r="3" fill="#FFF"/><circle cx="11" cy="23.5" r="3" fill="#FFF"/>'
        '<circle cx="21" cy="10" r="3" fill="#FFF"/>'
    ),
    "lock": (
        '<path d="M11.5 14v-3a4.5 4.5 0 0 1 9 0v3" fill="none" stroke="#FFF" stroke-width="2.6"/>'
        '<rect x="8.5" y="14" width="15" height="11" rx="2.5" fill="#FFF"/>'
        '<circle cx="16" cy="19.5" r="1.8" fill="currentColor"/>'
    ),
    "zip": "".join(
        f'<rect x="{13 if i % 2 else 16}" y="{6 + i * 3}" width="3" height="2" fill="#FFF"/>' for i in range(5)
    ) + '<rect x="12.5" y="21" width="7" height="6" rx="1.5" fill="#FFF"/>',
    "grid": (
        '<rect x="7.5" y="9" width="17" height="15" rx="2" fill="#FFF"/>'
        '<path d="M7.5 14h17M7.5 19h17M13.5 9v15M19 9v15" stroke="currentColor" stroke-width="1.4"/>'
    ),
    "play": '<path d="M12 9.5v14l11-7z" fill="#FFF" stroke="#FFF" stroke-width="1.5" stroke-linejoin="round"/>',
    "note": (
        '<path d="M13 22V10l10-2.5v12" fill="none" stroke="#FFF" stroke-width="2.4" stroke-linejoin="round"/>'
        '<ellipse cx="10.8" cy="22.3" rx="3.2" ry="2.6" fill="#FFF"/>'
        '<ellipse cx="20.8" cy="19.8" rx="3.2" ry="2.6" fill="#FFF"/>'
    ),
    "check": (
        '<path d="M8.5 16.5l5 5 10-11" fill="none" stroke="#FFF" stroke-width="3.6" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "container": "".join(
        f'<rect x="{x}" y="{y}" width="5.4" height="4.6" rx="1" fill="#FFF"/>'
        for x, y in [(7.5, 17.5), (13.3, 17.5), (19.1, 17.5), (10.4, 12.4), (16.2, 12.4), (13.3, 7.3)]
    ) + '<path d="M6 23.5h20" stroke="#FFF" stroke-width="2" stroke-linecap="round"/>',
    "info": (
        '<circle cx="16" cy="9.5" r="2.4" fill="#FFF"/>'
        '<path d="M16 14v10" stroke="#FFF" stroke-width="3.6" stroke-linecap="round"/>'
    ),
    "react": (
        '<g fill="none" stroke="currentColor" stroke-width="1.5">'
        '<ellipse cx="16" cy="16.5" rx="10" ry="4"/>'
        '<ellipse cx="16" cy="16.5" rx="10" ry="4" transform="rotate(60 16 16.5)"/>'
        '<ellipse cx="16" cy="16.5" rx="10" ry="4" transform="rotate(-60 16 16.5)"/></g>'
        '<circle cx="16" cy="16.5" r="2.2" fill="currentColor"/>'
    ),
}


# ------------------------------------------------------------------ formas --
def _defs(uid: str, base: str) -> str:
    return (
        f'<defs>'
        f'<linearGradient id="b{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{light(base, .35)}"/>'
        f'<stop offset=".5" stop-color="{base}"/>'
        f'<stop offset="1" stop-color="{dark(base, .22)}"/></linearGradient>'
        f'<linearGradient id="g{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#FFF" stop-opacity=".75"/>'
        f'<stop offset="1" stop-color="#FFF" stop-opacity=".08"/></linearGradient>'
        f'<filter id="d{uid}" x="-10%" y="-10%" width="120%" height="130%">'
        f'<feDropShadow dx="0" dy="1" stdDeviation="0" flood-color="#000" flood-opacity=".25"/></filter>'
        f'</defs>'
    )


def _label(text: str, color: str) -> str:
    n = len(text)
    size = {1: 17, 2: 14, 3: 11.5}.get(n, 10)
    fit = ' textLength="25" lengthAdjust="spacingAndGlyphs"' if n >= 3 else ""
    common = (f'x="16" y="{17 + size * .36:.1f}" text-anchor="middle" font-family="{FONT}" '
              f'font-weight="800" font-size="{size}"{fit}')
    shadow_color = "#000" if color.upper() in ("#FFF", "#FFFFFF") else "#FFF"
    text = html.escape(text)
    return (f'<text {common} dy="1" fill="{shadow_color}" fill-opacity=".3">{text}</text>'
            f'<text {common} fill="{color}">{text}</text>')


def tile(uid: str, base: str, label: str = "", glyph: str = "", fg: str = "#FFF") -> str:
    """Ladrilho de vidro arredondado com brilho na metade superior."""
    inner = _label(label, fg) if label else ""
    if glyph:
        inner = (f'<g color="{dark(base, .25)}" filter="url(#d{uid})">'
                 f'{GLYPHS[glyph]}</g>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">{_defs(uid, base)}'
        f'<rect x="1.5" y="1.5" width="29" height="29" rx="7" fill="url(#b{uid})" stroke="{dark(base, .35)}" stroke-width="1"/>'
        f'<path d="M3 9a6 6 0 0 1 6-6h14a6 6 0 0 1 6 6v5.5C21 17 11 17 3 14.5z" fill="url(#g{uid})"/>'
        f'<rect x="2.5" y="2.5" width="27" height="27" rx="6" fill="none" stroke="#FFF" stroke-opacity=".35"/>'
        f'{inner}</svg>'
    )


def sky_tile(uid: str) -> str:
    """Ícone de imagem: mini paisagem Aero (céu, sol e colina)."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><defs>'
        f'<linearGradient id="s{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#1D7FD1"/><stop offset="1" stop-color="#9ADBF8"/></linearGradient>'
        f'<linearGradient id="h{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#A8EC6A"/><stop offset="1" stop-color="#2E8A36"/></linearGradient>'
        f'<linearGradient id="g{uid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="#FFF" stop-opacity=".7"/><stop offset="1" stop-color="#FFF" stop-opacity="0"/></linearGradient>'
        f'<clipPath id="c{uid}"><rect x="1.5" y="1.5" width="29" height="29" rx="7"/></clipPath></defs>'
        f'<g clip-path="url(#c{uid})"><rect width="32" height="32" fill="url(#s{uid})"/>'
        f'<circle cx="22" cy="10" r="4" fill="#FFFBE0"/>'
        f'<path d="M0 22c6-5 12-5 18 0s10 3 14 0v10H0z" fill="url(#h{uid})"/>'
        f'<path d="M3 9a6 6 0 0 1 6-6h14a6 6 0 0 1 6 6v4C21 16 11 16 3 13.5z" fill="url(#g{uid})"/></g>'
        f'<rect x="1.5" y="1.5" width="29" height="29" rx="7" fill="none" stroke="#14598F"/>'
        f'<rect x="2.5" y="2.5" width="27" height="27" rx="6" fill="none" stroke="#FFF" stroke-opacity=".4"/></svg>'
    )


def doc(uid: str, base: str, lines: bool = True) -> str:
    """Documento genérico de vidro com canto dobrado."""
    body = "M7 2.5h12l7 7v18a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-23a2 2 0 0 1 2-2z"
    rows = "".join(f'<rect x="9" y="{y}" width="{w}" height="1.8" rx=".9" fill="{dark(base, .35)}" fill-opacity=".55"/>'
                   for y, w in [(14, 14), (18, 12), (22, 14)]) if lines else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">{_defs(uid, base)}'
        f'<path d="{body}" fill="url(#b{uid})" stroke="{dark(base, .4)}"/>'
        f'<path d="M6 4.5a2 2 0 0 1 2-2h11l3 3v7C16 15 10 14 6 12.5z" fill="url(#g{uid})"/>'
        f'<path d="M19 2.5v5a2 2 0 0 0 2 2h5" fill="{light(base, .6)}" stroke="{dark(base, .4)}" stroke-linejoin="round"/>'
        f'{rows}</svg>'
    )


def folder(uid: str, base: str, opened: bool = False) -> str:
    """Pasta aqua de vidro (fechada ou aberta)."""
    back = "M2.5 8a2.5 2.5 0 0 1 2.5-2.5h7l3 3h12a2.5 2.5 0 0 1 2.5 2.5v14.5a2.5 2.5 0 0 1-2.5 2.5H5a2.5 2.5 0 0 1-2.5-2.5z"
    if opened:
        front = "M6.5 13.5h23.2a1.5 1.5 0 0 1 1.4 2l-3.4 10.3a2.5 2.5 0 0 1-2.4 1.7H4.5a1.5 1.5 0 0 1-1.4-2l3.4-10.3a1.5 1.5 0 0 1 1.4-1.7z"
        gloss = "M6.7 14.5h22.6l-1.6 4.8C20 21 11 20.5 5.4 18.5z"
    else:
        front = "M2.5 12.5a2 2 0 0 1 2-2h23a2 2 0 0 1 2 2v12.5a2.5 2.5 0 0 1-2.5 2.5H5a2.5 2.5 0 0 1-2.5-2.5z"
        gloss = "M3.5 12.5a1.2 1.2 0 0 1 1.2-1.2h22.6a1.2 1.2 0 0 1 1.2 1.2v5C21 20 11 20 3.5 17.5z"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">{_defs(uid, base)}'
        f'<path d="{back}" fill="{dark(base, .18)}" stroke="{dark(base, .4)}"/>'
        f'<path d="{front}" fill="url(#b{uid})" stroke="{dark(base, .38)}"/>'
        f'<path d="{gloss}" fill="url(#g{uid})"/></svg>'
    )


# ------------------------------------------------------------- catálogo --
# id -> (tipo, cor, rótulo/glifo, cor do texto)
YELLOW_TEXT = "#3A2E00"
FILES = {
    "file":       ("doc", "#E8F2F8", False),
    "text":       ("doc", "#DDEBF3", True),
    "log":        ("doc", "#E9DFC9", True),
    "typescript": ("tile", "#2F74C0", "TS"),
    "tsx":        ("tile", "#2F74C0", "", "react"),
    "dts":        ("tile", "#1F8A9E", "DT"),
    "javascript": ("tile", "#EBC51E", "JS", YELLOW_TEXT),
    "jsx":        ("tile", "#EBC51E", "", "react"),
    "php":        ("tile", "#777BB3", "PHP"),
    "blade":      ("tile", "#F0513F", "B"),
    "laravel":    ("tile", "#F0513F", "A"),
    "python":     ("tile", "#3776AB", "PY"),
    "json":       ("tile", "#F2A73B", "{}", YELLOW_TEXT),
    "markdown":   ("tile", "#3F8FD8", "MD"),
    "readme":     ("tile", "#2FA3E0", "", "info"),
    "css":        ("tile", "#2A6FD6", "#"),
    "scss":       ("tile", "#CD6799", "S"),
    "less":       ("tile", "#2B4F81", "L"),
    "html":       ("tile", "#E4602F", "<>"),
    "vue":        ("tile", "#41B883", "V"),
    "xml":        ("tile", "#26A69A", "XML"),
    "svg":        ("tile", "#FFB300", "SVG", YELLOW_TEXT),
    "yaml":       ("tile", "#D84343", "YML"),
    "config":     ("tile", "#78909C", "", "gear"),
    "sql":        ("tile", "#EF8F00", "", "database"),
    "shell":      ("tile", "#37474F", "", "terminal"),
    "env":        ("tile", "#E5C93A", "ENV", YELLOW_TEXT),
    "docker":     ("tile", "#2496ED", "", "container"),
    "git":        ("tile", "#F05133", "", "branch"),
    "lock":       ("tile", "#8D9BA6", "", "lock"),
    "npm":        ("tile", "#CB3837", "npm"),
    "composer":   ("tile", "#8C5A2B", "C"),
    "vite":       ("tile", "#8E5CF7", "VI"),
    "test":       ("tile", "#43A047", "", "check"),
    "image":      ("sky",),
    "pdf":        ("tile", "#E53935", "PDF"),
    "archive":    ("tile", "#8D6E63", "", "zip"),
    "sheet":      ("tile", "#2E7D32", "", "grid"),
    "video":      ("tile", "#7E57C2", "", "play"),
    "audio":      ("tile", "#EC407A", "", "note"),
    "font":       ("tile", "#5C6BC0", "Aa"),
    "lua":        ("tile", "#2C2D72", "LU"),
    "go":         ("tile", "#00ADD8", "GO"),
    "rust":       ("tile", "#B7410E", "RS"),
    "java":       ("tile", "#E76F00", "JV"),
    "c":          ("tile", "#5C7CBA", "C"),
    "cpp":        ("tile", "#00599C", "C+"),
    "csharp":     ("tile", "#68217A", "C#"),
    "ruby":       ("tile", "#CC342D", "RB"),
    "license":    ("tile", "#C9A227", "©", YELLOW_TEXT),
}

FOLDERS = {
    "folder":      "#3FA9E0",
    "folder-src":  "#4CAF50",
    "folder-app":  "#26A69A",
    "folder-config": "#78909C",
    "folder-public": "#F5A623",
    "folder-assets": "#EC6FA8",
    "folder-test": "#9CCC2E",
    "folder-vendor": "#A1887F",
    "folder-git":  "#F05133",
    "folder-ide":  "#1E88E5",
    "folder-docs": "#64B5F6",
    "folder-db":   "#FFB300",
    "folder-routes": "#9575CD",
    "folder-storage": "#90A4AE",
    "folder-scripts": "#546E7A",
    "folder-views": "#26C6DA",
    "folder-logic": "#5C6BC0",
    "folder-styles": "#BA68C8",
    "folder-docker": "#2496ED",
}

FILE_EXTENSIONS = {
    "ts": "typescript", "mts": "typescript", "cts": "typescript", "d.ts": "dts",
    "tsx": "tsx", "js": "javascript", "mjs": "javascript", "cjs": "javascript", "jsx": "jsx",
    "php": "php", "phtml": "php", "blade.php": "blade",
    "py": "python", "pyw": "python", "pyi": "python",
    "json": "json", "jsonc": "json", "json5": "json", "webmanifest": "json",
    "md": "markdown", "markdown": "markdown", "mdx": "markdown",
    "css": "css", "scss": "scss", "sass": "scss", "less": "less",
    "html": "html", "htm": "html", "xhtml": "html", "vue": "vue",
    "xml": "xml", "xsd": "xml", "xsl": "xml", "plist": "xml", "svg": "svg",
    "yml": "yaml", "yaml": "yaml",
    "toml": "config", "ini": "config", "conf": "config", "cfg": "config", "neon": "config",
    "properties": "config", "htaccess": "config",
    "sql": "sql", "sqlite": "sql", "db": "sql",
    "sh": "shell", "bash": "shell", "zsh": "shell", "fish": "shell", "ps1": "shell", "bat": "shell", "cmd": "shell",
    "env": "env", "dockerfile": "docker", "lock": "lock",
    "test.ts": "test", "spec.ts": "test", "test.js": "test", "spec.js": "test",
    "test.tsx": "test", "spec.tsx": "test", "test.php": "test",
    "png": "image", "jpg": "image", "jpeg": "image", "gif": "image", "webp": "image",
    "ico": "image", "bmp": "image", "avif": "image", "tif": "image", "tiff": "image",
    "pdf": "pdf",
    "zip": "archive", "tar": "archive", "gz": "archive", "tgz": "archive", "rar": "archive",
    "7z": "archive", "bz2": "archive", "xz": "archive", "vsix": "archive",
    "csv": "sheet", "tsv": "sheet", "xlsx": "sheet", "xls": "sheet", "ods": "sheet",
    "mp4": "video", "mov": "video", "webm": "video", "mkv": "video", "avi": "video",
    "mp3": "audio", "wav": "audio", "ogg": "audio", "flac": "audio", "m4a": "audio",
    "ttf": "font", "otf": "font", "woff": "font", "woff2": "font", "eot": "font",
    "lua": "lua", "luau": "lua", "go": "go", "rs": "rust", "java": "java",
    "c": "c", "h": "c", "cpp": "cpp", "cc": "cpp", "hpp": "cpp", "cs": "csharp", "rb": "ruby",
    "txt": "text", "log": "log",
}

FILE_NAMES = {
    "package.json": "npm", "package-lock.json": "lock", "npm-shrinkwrap.json": "lock",
    "yarn.lock": "lock", "pnpm-lock.yaml": "lock", "composer.json": "composer", "composer.lock": "lock",
    "readme.md": "readme", "readme": "readme", "readme.txt": "readme",
    "license": "license", "license.md": "license", "license.txt": "license",
    "changelog.md": "markdown",
    "dockerfile": "docker", "docker-compose.yml": "docker", "docker-compose.yaml": "docker",
    "compose.yml": "docker", "compose.yaml": "docker", ".dockerignore": "docker",
    ".gitignore": "git", ".gitattributes": "git", ".gitmodules": "git", ".gitkeep": "git",
    ".env": "env", ".env.example": "env", ".env.local": "env", ".env.development": "env",
    ".env.production": "env", ".env.test": "env", ".env.testing": "env", ".env.sample": "env",
    ".env.backup": "env",
    "artisan": "laravel",
    "vite.config.js": "vite", "vite.config.ts": "vite", "vite.config.mjs": "vite",
    "phpunit.xml": "test", "phpunit.xml.dist": "test", "pest.php": "test",
    ".editorconfig": "config", ".prettierrc": "config", ".eslintrc": "config", ".eslintrc.json": "config",
    ".eslintrc.js": "config", "eslint.config.js": "config", "phpstan.neon": "config",
    "phpcs.xml": "config", "rector.php": "config", "pint.json": "config", "tsconfig.json": "config",
    "jsconfig.json": "config", ".htaccess": "config", "makefile": "config", ".npmrc": "config",
    ".nvmrc": "config", "tailwind.config.js": "config", "postcss.config.js": "config",
}

LANGUAGE_IDS = {
    "typescript": "typescript", "typescriptreact": "tsx", "javascript": "javascript",
    "javascriptreact": "jsx", "php": "php", "blade": "blade", "python": "python",
    "json": "json", "jsonc": "json", "markdown": "markdown", "css": "css", "scss": "scss",
    "less": "less", "html": "html", "vue": "vue", "xml": "xml", "yaml": "yaml", "sql": "sql",
    "shellscript": "shell", "dockerfile": "docker", "dockercompose": "docker", "ignore": "git",
    "ini": "config", "properties": "config", "lua": "lua", "go": "go", "rust": "rust",
    "java": "java", "c": "c", "cpp": "cpp", "csharp": "csharp", "ruby": "ruby", "log": "log",
    "dotenv": "env",
}

FOLDER_NAMES = {
    "folder-src": ["src", "source", "lib", "libs"],
    "folder-app": ["app", "application"],
    "folder-config": ["config", "conf", ".config", "settings", "bootstrap"],
    "folder-public": ["public", "www", "static", "dist", "build", "out"],
    "folder-assets": ["assets", "images", "img", "icons", "media", "fonts", "resources"],
    "folder-test": ["tests", "test", "__tests__", "spec", "specs", "e2e"],
    "folder-vendor": ["vendor", "node_modules", "packages", "bower_components"],
    "folder-git": [".git", ".github", ".gitlab", ".husky"],
    "folder-ide": [".vscode", ".idea", ".claude", ".devcontainer"],
    "folder-docs": ["docs", "doc", "documentation"],
    "folder-db": ["database", "migrations", "seeders", "seeds", "factories", "db", "sql"],
    "folder-routes": ["routes", "router", "api"],
    "folder-storage": ["storage", "logs", "cache", "tmp", "temp", ".cache"],
    "folder-scripts": ["scripts", "bin", "tools", "commands", "console"],
    "folder-views": ["views", "templates", "layouts", "components", "pages", "partials"],
    "folder-logic": ["models", "services", "controllers", "http", "jobs", "events",
                     "listeners", "providers", "middleware", "actions", "repositories"],
    "folder-styles": ["styles", "css", "scss", "sass", "themes"],
    "folder-docker": ["docker", ".docker"],
}


# ------------------------------------------------------------------ build --
def render_icons() -> dict:
    """Retorna {nome_do_arquivo_svg: conteúdo}."""
    out = {}
    for i, (name, spec) in enumerate(FILES.items()):
        uid = f"f{i}"
        kind = spec[0]
        if kind == "doc":
            out[f"{name}.svg"] = doc(uid, spec[1], spec[2])
        elif kind == "sky":
            out[f"{name}.svg"] = sky_tile(uid)
        else:
            base, text = spec[1], spec[2]
            glyph = spec[3] if len(spec) > 3 and spec[3] in GLYPHS else ""
            fg = spec[3] if len(spec) > 3 and spec[3].startswith("#") else "#FFF"
            out[f"{name}.svg"] = tile(uid, base, text, glyph, fg)
    for i, (name, base) in enumerate(FOLDERS.items()):
        out[f"{name}.svg"] = folder(f"d{i}", base)
        out[f"{name}-open.svg"] = folder(f"o{i}", base, opened=True)
    return out


def icon_theme() -> dict:
    defs = {f"_{n}": {"iconPath": f"../icons/{n}.svg"} for n in FILES}
    for n in FOLDERS:
        defs[f"_{n}"] = {"iconPath": f"../icons/{n}.svg"}
        defs[f"_{n}_open"] = {"iconPath": f"../icons/{n}-open.svg"}

    folder_names, folder_names_open = {}, {}
    for icon, names in FOLDER_NAMES.items():
        for n in names:
            folder_names[n] = f"_{icon}"
            folder_names_open[n] = f"_{icon}_open"

    return {
        "hidesExplorerArrows": False,
        "iconDefinitions": defs,
        "file": "_file",
        "folder": "_folder",
        "folderExpanded": "_folder_open",
        "rootFolder": "_folder",
        "rootFolderExpanded": "_folder_open",
        "fileExtensions": {k: f"_{v}" for k, v in FILE_EXTENSIONS.items()},
        "fileNames": {k: f"_{v}" for k, v in FILE_NAMES.items()},
        "languageIds": {k: f"_{v}" for k, v in LANGUAGE_IDS.items()},
        "folderNames": folder_names,
        "folderNamesExpanded": folder_names_open,
    }
