"""Regras de sintaxe: TextMate (``tokenColors``) e semânticas (``semanticTokenColors``)."""

# (nome, papel, fontStyle, escopos)
TEXTMATE_RULES = [
    ("Comentários", "comment", "italic", [
        "comment", "punctuation.definition.comment", "string.comment",
    ]),
    ("Doc tags", "keyword", "italic", [
        "comment storage.type", "comment keyword", "comment.block.documentation entity.name.type",
        "storage.type.class.jsdoc", "punctuation.definition.block.tag.jsdoc",
    ]),
    ("Keywords", "keyword", "", [
        "keyword", "keyword.control", "storage", "storage.type", "storage.modifier",
        "keyword.operator.new", "keyword.operator.expression", "keyword.operator.logical.python",
        "keyword.operator.word", "keyword.other.using", "keyword.other.import",
        "keyword.control.import", "keyword.control.from", "keyword.control.export",
    ]),
    ("Operadores", "operator", "", [
        "keyword.operator", "keyword.operator.assignment", "keyword.operator.arithmetic",
        "keyword.operator.comparison", "keyword.operator.relational", "keyword.operator.ternary",
        "keyword.operator.optional", "keyword.operator.spread", "keyword.operator.type.annotation",
        "punctuation.separator.key-value", "storage.type.function.arrow",
    ]),
    ("Pontuação", "punctuation", "", [
        "punctuation", "punctuation.separator", "punctuation.terminator", "punctuation.accessor",
        "meta.brace", "punctuation.definition.block", "punctuation.definition.parameters",
        "punctuation.section",
    ]),
    ("Strings", "string", "", [
        "string", "string.quoted", "string.template", "punctuation.definition.string",
        "string.unquoted.plain", "markup.inline.raw",
    ]),
    ("Interpolação", "keyword", "", [
        "punctuation.definition.template-expression", "punctuation.section.embedded",
        "punctuation.section.embedded.begin.php", "punctuation.section.embedded.end.php",
    ]),
    ("Escapes", "escape", "", [
        "constant.character.escape", "constant.character.format.placeholder",
        "constant.other.placeholder",
    ]),
    ("Regex", "regex", "", ["string.regexp", "constant.other.character-class.regexp"]),
    ("Números", "number", "", ["constant.numeric", "keyword.other.unit"]),
    ("Constantes", "constant", "", [
        "constant.language", "constant.other", "support.constant", "variable.other.constant",
        "variable.other.enummember", "entity.name.constant", "constant.other.symbol",
        "constant.language.boolean", "constant.language.null",
    ]),
    ("Tipos e classes", "type", "", [
        "entity.name.type", "entity.name.class", "entity.name.namespace", "entity.other.inherited-class",
        "support.type", "support.class", "storage.type.primitive", "entity.name.type.interface",
        "entity.name.type.alias", "entity.name.type.enum", "support.type.primitive",
        "entity.name.type.class.php", "support.other.namespace.php",
    ]),
    ("Funções", "function", "", [
        "entity.name.function", "support.function", "meta.function-call entity.name.function",
        "variable.function", "entity.name.method", "meta.method-call entity.name.function",
        "support.function.builtin", "entity.name.function.decorator", "meta.decorator",
    ]),
    ("Variáveis", "variable", "", [
        "variable", "variable.other", "variable.other.readwrite", "meta.definition.variable",
        "variable.other.php", "support.variable",
    ]),
    ("this / self", "keyword", "italic", [
        "variable.language", "variable.language.this", "variable.language.self",
        "variable.parameter.function.language.special.self.python",
    ]),
    ("Parâmetros", "parameter", "", [
        "variable.parameter", "meta.parameters variable", "variable.parameter.function",
    ]),
    ("Propriedades", "property", "", [
        "variable.other.property", "variable.other.object.property", "meta.object-literal.key",
        "support.type.property-name", "entity.name.tag.yaml", "variable.other.member",
        "meta.property-name", "support.variable.property",
    ]),
    ("JSON: chaves", "property", "", [
        "support.type.property-name.json", "meta.structure.dictionary.key.python",
    ]),
    ("Tags HTML/XML", "tag", "", [
        "entity.name.tag", "meta.tag.sgml", "punctuation.definition.tag",
        "support.class.component", "entity.name.tag.html",
    ]),
    ("Atributos", "attribute", "", [
        "entity.other.attribute-name", "entity.other.attribute-name.html",
    ]),
    ("CSS: seletores", "type", "", [
        "entity.other.attribute-name.class.css", "entity.other.attribute-name.id.css",
        "entity.other.attribute-name.pseudo-class.css", "entity.other.attribute-name.pseudo-element.css",
        "entity.name.tag.css", "entity.name.tag.reference.scss",
    ]),
    ("CSS: propriedades", "property", "", [
        "support.type.property-name.css", "support.type.vendored.property-name.css",
    ]),
    ("CSS: valores", "number", "", [
        "support.constant.property-value.css", "support.constant.color", "constant.other.color",
        "support.constant.font-name",
    ]),
    ("CSS: variáveis", "parameter", "", [
        "variable.css", "variable.scss", "variable.argument.css", "support.type.custom-property",
    ]),
    ("PHP: tags de abertura", "keyword", "", ["punctuation.section.embedded.begin.php",
                                              "punctuation.section.embedded.end.php"]),
    ("PHP: $", "variable", "", ["punctuation.definition.variable.php"]),
    ("Python: f-string", "keyword", "", ["storage.type.string.python"]),
    ("SQL", "keyword", "", ["keyword.other.DML.sql", "keyword.other.DDL.sql", "keyword.other.sql"]),
    ("Shell: variáveis", "parameter", "", ["variable.other.normal.shell", "variable.other.special.shell"]),
    # markdown / markup
    ("Títulos", "heading", "bold", [
        "markup.heading", "entity.name.section", "markup.heading.setext",
        "punctuation.definition.heading.markdown",
    ]),
    ("Negrito", "keyword", "bold", ["markup.bold", "punctuation.definition.bold"]),
    ("Itálico", "parameter", "italic", ["markup.italic", "punctuation.definition.italic"]),
    ("Tachado", "fgMuted", "strikethrough", ["markup.strikethrough"]),
    ("Links", "link", "underline", [
        "markup.underline.link", "string.other.link", "markup.link", "constant.other.reference.link",
    ]),
    ("Listas", "operator", "", ["punctuation.definition.list.begin.markdown", "markup.list.numbered"]),
    ("Citações", "comment", "italic", ["markup.quote", "punctuation.definition.quote.begin.markdown"]),
    ("Código inline", "string", "", ["markup.inline.raw.string.markdown", "markup.fenced_code.block"]),
    ("Diff inserido", "added", "", ["markup.inserted", "punctuation.definition.inserted"]),
    ("Diff removido", "deleted", "", ["markup.deleted", "punctuation.definition.deleted"]),
    ("Diff alterado", "modified", "", ["markup.changed", "punctuation.definition.changed"]),
    ("Diff cabeçalho", "type", "", ["meta.diff.header", "meta.diff.range"]),
    ("Inválido", "invalid", "", ["invalid", "invalid.illegal"]),
    ("Obsoleto", "fgMuted", "strikethrough", ["invalid.deprecated"]),
]

# papel -> fontStyle opcional
SEMANTIC_RULES = {
    "namespace": ("type", None),
    "class": ("type", None),
    "enum": ("type", None),
    "interface": ("type", None),
    "struct": ("type", None),
    "type": ("type", None),
    "typeParameter": ("type", "italic"),
    "parameter": ("parameter", None),
    "variable": ("variable", None),
    "variable.readonly": ("constant", None),
    "variable.defaultLibrary": ("constant", None),
    "property": ("property", None),
    "property.readonly": ("property", None),
    "enumMember": ("constant", None),
    "function": ("function", None),
    "method": ("function", None),
    "macro": ("function", None),
    "decorator": ("function", None),
    "keyword": ("keyword", None),
    "comment": ("comment", "italic"),
    "string": ("string", None),
    "number": ("number", None),
    "regexp": ("regex", None),
    "operator": ("operator", None),
    "selfKeyword": ("keyword", "italic"),
    "*.deprecated": (None, "strikethrough"),
}


def token_colors(p: dict) -> list:
    rules = []
    for name, role, style, scopes in TEXTMATE_RULES:
        settings = {"foreground": p[role]}
        if style:
            settings["fontStyle"] = style
        rules.append({"name": name, "scope": scopes, "settings": settings})
    return rules


def semantic_token_colors(p: dict) -> dict:
    out = {}
    for selector, (role, style) in SEMANTIC_RULES.items():
        if role is None:
            out[selector] = {"strikethrough": True}
            continue
        if style:
            out[selector] = {"foreground": p[role], "fontStyle": style}
        else:
            out[selector] = p[role]
    return out
