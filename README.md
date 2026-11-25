# Frutiger Aero Glass

Tema para VS Code na estética **Frutiger Aero**: céu, água, verde, vidro translúcido e brilho. Tem duas variantes:

- **Frutiger Aero Glass Dark**: vidro azul-lagoa com texto claro.
- **Frutiger Aero Glass Light**: vidro branco-gelo com texto escuro.

O projeto tem duas camadas independentes:

| Camada | O que faz | Precisa de |
|---|---|---|
| **1. Tema de cores** | Interface, sintaxe (TextMate + semântica) e terminal | Nada além do VS Code |
| **2. Aero Glass** | Céu de fundo, vidro translúcido, brilho, abas, pílulas verdes, orbs, widgets de vidro | Extensão *Custom CSS and JS Loader* |

A Camada 1 funciona sozinha. A Camada 2 só se aplica quando um tema `aeroglass` está ativo: trocar de tema desliga o efeito.

---

## Camada 1: instalar o tema

```sh
python3 build.py --vsix
code --install-extension dist/frutiger-aero-glass-0.1.0.vsix
```

No VS Code: `Ctrl+K Ctrl+T` → **Frutiger Aero Glass Dark** (ou Light).

## Camada 2: ativar o Aero Glass

> ⚠️ A camada 2 altera arquivos internos do VS Code por meio de uma extensão de terceiros. O VS Code passa a mostrar o aviso *"Your installation appears to be corrupt"*, e é preciso reativar o efeito depois de cada atualização do VS Code.

1. Instale a extensão **Custom CSS and JS Loader** (`be5invis.vscode-custom-css`).

2. Dê ao seu usuário permissão de escrita na instalação do VS Code. Instalado via `.deb`/apt, ele fica em `/usr/share/code`:

   ```sh
   sudo chown -R "$(whoami)" /usr/share/code
   ```

   O apt devolve a posse ao root a cada atualização, então repita este passo junto com o passo 5. A versão Snap é somente leitura e não funciona com o loader.

3. Gere o CSS (o SVG do céu vai embutido nele):

   ```sh
   python3 build.py
   ```

4. Em `settings.json`, aponte para o arquivo **gerado** (caminho absoluto):

   ```jsonc
   {
     "workbench.colorTheme": "Frutiger Aero Glass Dark",
     "window.titleBarStyle": "custom",
     "vscode_custom_css.imports": [
       "file:///CAMINHO/ATE/frutiger-aero-theme/dist/aero-glass.css"
     ]
   }
   ```

5. `Ctrl+Shift+P` → **Enable Custom CSS and JS**. Depois **feche e abra o VS Code** (só recarregar a janela não basta).

6. No aviso de instalação corrompida, escolha *Don't Show Again*.

| Situação | O que fazer |
|---|---|
| Editou `src/glass.css` | `python3 build.py`, depois **Reload Custom CSS and JS** e reinicie |
| O VS Code foi atualizado | Repita os passos 2 e 5 |
| Remover a camada 2 | **Disable Custom CSS and JS** e reinicie |

### Ajuste fino

As variáveis ficam no topo de [src/glass.css](src/glass.css):

- `--aero-blur` / `--aero-blur-widget`: intensidade do desfoque. Use `0px` se a GPU sofrer.
- `--aero-glass-editor`, `--aero-glass-side`, …: cor e opacidade de cada painel, por variante.
- `--aero-pill`, `--aero-button`, `--aero-activity`: gradientes brilhantes.

### Limitações conhecidas

- **Terminal**: o xterm desenha o fundo em canvas, então ele fica com a cor sólida do tema (sem vidro).
- **Menus de contexto**: ficam dentro de um *shadow DOM* que o CSS injetado não alcança e usam só as cores do tema.
- **Minimap**: o canvas é opaco. O CSS reduz a opacidade dele para não destoar.
- O CSS depende de classes internas do VS Code (testado com a versão 1.143). Uma atualização pode exigir ajustes.

---

## Desenvolvimento

Não usa Node. Basta Python 3.

```
build.py            gera tudo; --vsix também empacota
src/palettes.py     paletas DARK e LIGHT (papéis -> cores)
src/workbench.py    papéis -> chaves de cor da interface
src/tokens.py       papéis -> regras de sintaxe
src/background.py   gera assets/aero-sky.svg (papel de parede original)
src/glass.css       fonte da camada 2 (com marcadores)
themes/             temas gerados (não edite à mão)
dist/aero-glass.css CSS final da camada 2 (gerado)
samples/            arquivos para conferir as cores
```

O build confere o contraste WCAG (mínimo de 4.5:1 para texto) de todas as cores de sintaxe e das barras, e sai com erro se alguma ficar abaixo.

Para testar sem reinstalar, abra a pasta no VS Code e pressione `F5` (Extension Development Host).
# vscode-frutiger-aero-theme
# vscode-frutiger-aero-theme
