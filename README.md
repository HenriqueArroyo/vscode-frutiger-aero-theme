# Frutiger Aero Glass

Tema para VS Code na estética **Frutiger Aero**: céu, água, verde, vidro translúcido e brilho. Tem duas variantes:

- **Frutiger Aero Glass Dark**: vidro azul-lagoa com texto claro.
- **Frutiger Aero Glass Light**: vidro branco-gelo com texto escuro.

O projeto tem três camadas independentes:

| Camada | O que faz | Precisa de |
|---|---|---|
| **1. Tema de cores** | Interface, sintaxe (TextMate + semântica) e terminal | Só o VS Code |
| **2. Aero Glass** | Céu de fundo, vidro translúcido, brilho, abas, pílulas verdes, orbs, widgets de vidro | Extensão *Custom CSS and JS Loader* |
| **3. Ícones de arquivo** | Ladrilhos de vidro com brilho por linguagem e pastas aqua coloridas por função | Só o VS Code |

As Camadas 1 e 3 vêm na mesma extensão e funcionam sozinhas. A Camada 2 é opcional e só se aplica quando um tema `aeroglass` está ativo: trocar de tema desliga o efeito.

---

## Instalação completa

### Pré-requisitos

- **VS Code** 1.80 ou mais recente.
- **Git**, para clonar o repositório.
- **Python 3.8+**, para gerar o pacote `.vsix`. O projeto não usa Node.

### Passo 1: baixar o projeto e gerar a extensão

```sh
git clone https://github.com/HenriqueArroyo/vscode-frutiger-aero-theme.git
cd vscode-frutiger-aero-theme
python3 build.py --vsix
```

No Windows, use `py build.py --vsix`.

O `.vsix` não fica versionado no repositório: ele é gerado em `dist/frutiger-aero-glass-<versão>.vsix`.

### Passo 2: instalar a extensão (Camadas 1 e 3)

```sh
code --install-extension dist/frutiger-aero-glass-0.2.0.vsix
```

Também dá para instalar pela interface: aba **Extensions** → menu `…` → **Install from VSIX…** → escolha o arquivo.

### Passo 3: ativar as cores e os ícones

- **Cores:** `Ctrl+K Ctrl+T` → **Frutiger Aero Glass Dark** (ou **Light**).
- **Ícones:** `Ctrl+Shift+P` → **Preferences: File Icon Theme** → **Frutiger Aero Glass Icons**.

Se você não quiser a Camada 2, a instalação termina aqui.

### Passo 4 (opcional): ativar o Aero Glass (Camada 2)

> ⚠️ A Camada 2 altera arquivos internos do VS Code por meio de uma extensão de terceiros. O VS Code passa a mostrar o aviso *"Your installation appears to be corrupt"*, e é preciso reativar o efeito depois de cada atualização do VS Code. Para desfazer, veja [Desinstalar](#desinstalar).

**4.1. Instale o loader.** Na aba Extensions, procure por **Custom CSS and JS Loader** (`be5invis.vscode-custom-css`), ou rode:

```sh
code --install-extension be5invis.vscode-custom-css
```

**4.2. Libere a escrita na pasta de instalação do VS Code.** O loader precisa alterar arquivos dela, e o passo depende do sistema:

| Sistema / forma de instalação | O que fazer |
|---|---|
| Linux, `.deb`/apt (`/usr/share/code`) | `sudo chown -R "$(whoami)" /usr/share/code` |
| Linux, `.rpm` (`/usr/share/code`) | o mesmo comando acima |
| Linux, Snap ou Flatpak | **Não funciona**: a instalação é somente leitura. Use o pacote `.deb`/`.rpm` |
| macOS | `sudo chown -R "$(whoami)" "/Applications/Visual Studio Code.app"` |
| Windows, *User Installer* (padrão) | Nada a fazer: a pasta já pertence ao seu usuário |
| Windows, *System Installer* | Abra o VS Code **como administrador** só para executar o passo 4.5 |

Confira no Linux: `ls -ld /usr/share/code` deve mostrar o seu usuário, não `root`.

**4.3. Localize o CSS.** O arquivo `dist/aero-glass.css` já vem pronto no repositório, com o céu SVG embutido. Você só precisa do caminho absoluto dele. Se alterar `src/glass.css`, rode `python3 build.py` para gerá-lo de novo.

**4.4. Edite o `settings.json` de usuário.** Abra com `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**. O arquivo fica em:

- Linux: `~/.config/Code/User/settings.json`
- macOS: `~/Library/Application Support/Code/User/settings.json`
- Windows: `%APPDATA%\Code\User\settings.json`

Acrescente as chaves abaixo, ajustando o caminho. Lembre da vírgula depois da última chave que já existia.

```jsonc
{
  "workbench.colorTheme": "Frutiger Aero Glass Dark",
  "workbench.iconTheme": "aeroglass-icons",
  "window.titleBarStyle": "custom",
  "vscode_custom_css.imports": [
    "file:///home/SEU_USUARIO/vscode-frutiger-aero-theme/dist/aero-glass.css"
  ]
}
```

| Sistema | Exemplo de caminho |
|---|---|
| Linux | `file:///home/ana/vscode-frutiger-aero-theme/dist/aero-glass.css` |
| macOS | `file:///Users/ana/vscode-frutiger-aero-theme/dist/aero-glass.css` |
| Windows | `file:///C:/Users/ana/vscode-frutiger-aero-theme/dist/aero-glass.css` |

**4.5. Ative o loader.** `Ctrl+Shift+P` → **Enable Custom CSS and JS**. Deve aparecer uma mensagem pedindo para reiniciar.

**4.6. Reinicie por completo.** Feche **todas** as janelas do VS Code e abra de novo. Só recarregar a janela não basta.

**4.7. Silencie o aviso.** No aviso *"Your installation appears to be corrupt"*, escolha **Don't Show Again**.

---

## Manutenção

| Situação | O que fazer |
|---|---|
| Atualizou o repositório (`git pull`) | `python3 build.py --vsix`, reinstale o `.vsix` (passo 2), depois **Reload Custom CSS and JS** e reinicie |
| Editou `src/glass.css` | `python3 build.py`, depois **Reload Custom CSS and JS** e reinicie |
| O VS Code foi atualizado | Repita os passos 4.2 e 4.5 e reinicie |

## Desinstalar

1. **Camada 2:** `Ctrl+Shift+P` → **Disable Custom CSS and JS**, reinicie e, se quiser, desinstale o loader.
2. **Camadas 1 e 3:** escolha outro tema de cores e de ícones e desinstale a extensão **Frutiger Aero Glass** na aba Extensions, ou rode `code --uninstall-extension local.frutiger-aero-glass`.
3. Remova `window.titleBarStyle` e `vscode_custom_css.imports` do `settings.json`.

## Problemas comuns

| Sintoma | Causa provável e solução |
|---|---|
| Reiniciei e nada mudou | O loader não conseguiu gravar na instalação do VS Code. Refaça o passo 4.2 e depois o 4.5. Ao rodar *Enable*, veja se aparece um erro de permissão |
| O vidro sumiu depois de uma atualização | Atualizações do VS Code restauram os arquivos originais. Repita os passos 4.2 e 4.5 |
| Só as cores mudaram, sem céu nem vidro | O tema ativo não é um `aeroglass` ou o caminho em `vscode_custom_css.imports` está errado. Confira se ele começa com `file:///` e aponta para `dist/aero-glass.css` |
| A barra de título ficou sem brilho ou sem orbs | Falta `"window.titleBarStyle": "custom"` |
| Lentidão ao rolar | Diminua o desfoque: `--aero-blur: 0px` em `src/glass.css`, depois `python3 build.py` e **Reload Custom CSS and JS** |

---

## Personalização

### Vidro (Camada 2)

As variáveis ficam no topo de [src/glass.css](src/glass.css):

- `--aero-blur` / `--aero-blur-widget`: intensidade do desfoque. Use `0px` se a GPU sofrer.
- `--aero-glass-editor`, `--aero-glass-side`, …: cor e opacidade de cada painel, por variante.
- `--aero-pill`, `--aero-button`, `--aero-activity`: gradientes brilhantes.

### Ícones (Camada 3)

O que já está coberto:

- **Linguagens:** TS/TSX, JS/JSX, PHP, Blade, Python, JSON, Markdown, CSS/SCSS/Less, HTML, Vue, XML, SVG, YAML, SQL, shell, Lua/Luau, Go, Rust, Java, C/C++, C#, Ruby.
- **Formatos:** imagens (mini paisagem Aero), PDF, planilhas, arquivos compactados, vídeo, áudio, fontes, texto e log.
- **Arquivos especiais:** `package.json`, `composer.json`, lockfiles, `.env*`, `Dockerfile`/`docker-compose`, `.gitignore`, `artisan`, `vite.config.*`, `phpunit.xml`, `README`, `LICENSE` e configs (`tsconfig`, `phpstan.neon`, `.editorconfig`…).
- **Pastas com cor por função:** código (`src`, `app`), configuração, `public`/`dist`, assets, testes, dependências (`vendor`, `node_modules`), git, IDE (`.vscode`), documentação, banco de dados, `routes`, `storage`, scripts, views, lógica (`models`, `services`, `controllers`…), estilos e docker.

Para incluir uma extensão, um nome de arquivo ou uma pasta, edite os mapas em [src/icons.py](src/icons.py), rode `python3 build.py --vsix` e reinstale.

### Limitações conhecidas

- **Terminal**: o xterm desenha o fundo em canvas, então ele fica com a cor sólida do tema (sem vidro).
- **Menus de contexto**: ficam dentro de um *shadow DOM* que o CSS injetado não alcança e usam só as cores do tema.
- **Minimap**: o canvas é opaco. O CSS reduz a opacidade dele para não destoar.
- O CSS depende de classes internas do VS Code (testado com a versão 1.143). Uma atualização pode exigir ajustes.

---

## Desenvolvimento

```
build.py            gera tudo; --vsix também empacota
src/palettes.py     paletas DARK e LIGHT (papéis -> cores)
src/workbench.py    papéis -> chaves de cor da interface
src/tokens.py       papéis -> regras de sintaxe
src/background.py   gera assets/aero-sky.svg (papel de parede original)
src/glass.css       fonte da camada 2 (com marcadores)
src/icons.py        camada 3: desenho dos ícones e mapas extensão/nome/pasta -> ícone
icons/              SVGs dos ícones (gerados)
themes/             temas de cores e de ícones gerados (não edite à mão)
dist/aero-glass.css CSS final da camada 2 (gerado)
samples/            arquivos para conferir as cores
```

O build confere o contraste WCAG (mínimo de 4.5:1 para texto) de todas as cores de sintaxe e das barras, e sai com erro se alguma ficar abaixo.

Para testar sem reinstalar, abra a pasta no VS Code e pressione `F5` (Extension Development Host). A janela de teste abre com a pasta `samples/`.
