"""Mapeamento papel -> chaves de cor da interface (workbench) do VS Code."""


def a(color: str, alpha: str) -> str:
    """Troca/aplica o canal alfa (``alpha`` em hex de 2 dígitos)."""
    return color[:7] + alpha


def workbench_colors(p: dict) -> dict:
    dark = p["kind"] == "dark"
    c = {}

    # --- base ---------------------------------------------------------------
    c.update({
        "focusBorder": a(p["accent"], "99"),
        "foreground": p["fg"],
        "disabledForeground": p["fgDim"],
        "descriptionForeground": p["fgMuted"],
        "errorForeground": p["error"],
        "icon.foreground": p["fgMuted"],
        "selection.background": p["selection"],
        "widget.shadow": p["shadow"],
        "widget.border": p["border"],
        "sash.hoverBorder": p["accent"],
        "contrastBorder": "#00000000",
        "textLink.foreground": p["link"],
        "textLink.activeForeground": p["accent"],
        "textPreformat.foreground": p["string"],
        "textPreformat.background": a(p["bgDeep"], "AA"),
        "textBlockQuote.background": a(p["bgDeep"], "88"),
        "textBlockQuote.border": p["accent"],
        "textCodeBlock.background": a(p["bgDeep"], "AA"),
        "textSeparator.foreground": p["border"],
        "window.activeBorder": p["borderStrong"],
        "window.inactiveBorder": p["border"],
    })

    # --- barra de título / command center ------------------------------------
    c.update({
        "titleBar.activeBackground": p["titleBg"],
        "titleBar.activeForeground": p["titleFg"],
        "titleBar.inactiveBackground": p["titleBg"],
        "titleBar.inactiveForeground": a(p["titleFg"], "99"),
        "titleBar.border": p["border"],
        "commandCenter.background": a(p["bgInput"], "99" if dark else "CC"),
        "commandCenter.foreground": p["titleFg"],
        "commandCenter.border": p["borderStrong"],
        "commandCenter.activeBackground": a(p["bgInput"], "CC" if dark else "FF"),
        "commandCenter.activeForeground": p["titleFg"],
        "commandCenter.activeBorder": p["accent"],
        "commandCenter.inactiveForeground": a(p["titleFg"], "99"),
        "commandCenter.inactiveBorder": p["border"],
        "menubar.selectionBackground": p["bgHover"],
        "menubar.selectionForeground": p["titleFg"],
    })

    # --- barra de atividades --------------------------------------------------
    c.update({
        "activityBar.background": p["activityBg"],
        "activityBar.foreground": p["activityFg"],
        "activityBar.inactiveForeground": p["activityInactiveFg"],
        "activityBar.border": "#00000000",
        "activityBar.activeBorder": "#FFFFFF",
        "activityBar.activeBackground": "#FFFFFF26",
        "activityBar.activeFocusBorder": "#FFFFFF",
        "activityBar.dropBorder": "#FFFFFF",
        "activityBarBadge.background": p["accent2"] if dark else "#FFFFFF",
        "activityBarBadge.foreground": "#0B3320" if dark else p["activityBg"],
        "activityBarTop.foreground": p["fg"],
        "activityBarTop.activeBorder": p["accent"],
        "activityBarTop.inactiveForeground": p["fgMuted"],
    })

    # --- barra lateral --------------------------------------------------------
    c.update({
        "sideBar.background": p["bgAlt"],
        "sideBar.foreground": p["fg"],
        "sideBar.border": p["border"],
        "sideBar.dropBackground": a(p["accent"], "33"),
        "sideBarTitle.foreground": p["fg"],
        "sideBarTitle.background": p["bgAlt"],
        "sideBarSectionHeader.background": p["headerBg"],
        "sideBarSectionHeader.foreground": p["headerFg"],
        "sideBarSectionHeader.border": "#00000000",
        "sideBarActivityBarTop.border": p["border"],
        "sideBarStickyScroll.background": p["bgAlt"],
        "sideBarStickyScroll.shadow": p["shadow"],
    })

    # --- listas e árvores -----------------------------------------------------
    c.update({
        "list.activeSelectionBackground": p["bgActive"],
        "list.activeSelectionForeground": p["fg"],
        "list.activeSelectionIconForeground": p["fg"],
        "list.inactiveSelectionBackground": a(p["accent"], "26"),
        "list.inactiveSelectionForeground": p["fg"],
        "list.hoverBackground": p["bgHover"],
        "list.hoverForeground": p["fg"],
        "list.focusBackground": a(p["accent"], "33"),
        "list.focusForeground": p["fg"],
        "list.focusOutline": a(p["accent"], "99"),
        "list.inactiveFocusOutline": a(p["accent"], "44"),
        "list.highlightForeground": p["accent"] if dark else "#0F6FA8",
        "list.focusHighlightForeground": p["accent"] if dark else "#0F6FA8",
        "list.dropBackground": a(p["accent"], "33"),
        "list.errorForeground": p["error"],
        "list.warningForeground": p["warning"],
        "list.invalidItemForeground": p["error"],
        "tree.indentGuidesStroke": a(p["fgMuted"], "55"),
        "tree.inactiveIndentGuidesStroke": a(p["fgMuted"], "26"),
    })

    # --- grupos de editor e abas ---------------------------------------------
    c.update({
        "editorGroup.border": p["border"],
        "editorGroup.dropBackground": a(p["accent"], "26"),
        "editorGroup.emptyBackground": p["bg"],
        "editorGroupHeader.tabsBackground": p["tabInactiveBg"],
        "editorGroupHeader.tabsBorder": p["border"],
        "editorGroupHeader.noTabsBackground": p["bg"],
        "editorGroupHeader.border": p["border"],
        "tab.activeBackground": p["tabActiveBg"],
        "tab.activeForeground": p["tabActiveFg"],
        "tab.activeBorder": "#00000000",
        "tab.activeBorderTop": p["accent"],
        "tab.inactiveBackground": p["tabInactiveBg"],
        "tab.inactiveForeground": p["tabInactiveFg"],
        "tab.border": p["border"],
        "tab.hoverBackground": a(p["tabActiveBg"], "AA"),
        "tab.hoverForeground": p["tabActiveFg"],
        "tab.unfocusedActiveBackground": a(p["tabActiveBg"], "CC"),
        "tab.unfocusedActiveForeground": a(p["tabActiveFg"], "BB"),
        "tab.unfocusedInactiveForeground": a(p["tabInactiveFg"], "99"),
        "tab.unfocusedActiveBorderTop": a(p["accent"], "66"),
        "tab.modifiedBorder": p["warning"],
        "tab.activeModifiedBorder": p["warning"],
        "tab.lastPinnedBorder": p["borderStrong"],
        "breadcrumb.foreground": p["fgMuted"],
        "breadcrumb.focusForeground": p["fg"],
        "breadcrumb.activeSelectionForeground": p["accent"],
        "breadcrumb.background": p["bg"],
        "breadcrumbPicker.background": p["bgWidget"],
    })

    # --- editor ---------------------------------------------------------------
    c.update({
        "editor.background": p["bg"],
        "editor.foreground": p["fg"],
        "editorLineNumber.foreground": a(p["fgDim"], "CC"),
        "editorLineNumber.activeForeground": p["fg"],
        "editorCursor.foreground": p["accent"] if dark else "#0F6FA8",
        "editor.selectionBackground": p["selection"],
        "editor.inactiveSelectionBackground": a(p["accent"], "26"),
        "editor.selectionHighlightBackground": p["wordHighlight"],
        "editor.selectionHighlightBorder": "#00000000",
        "editor.wordHighlightBackground": p["wordHighlight"],
        "editor.wordHighlightStrongBackground": a(p["accent2"], "33"),
        "editor.findMatchBackground": p["findMatch"],
        "editor.findMatchHighlightBackground": p["findMatchHighlight"],
        "editor.findRangeHighlightBackground": a(p["accent"], "14"),
        "editor.findMatchBorder": p["string"],
        "editor.lineHighlightBackground": p["lineHighlight"],
        "editor.lineHighlightBorder": "#00000000",
        "editor.rangeHighlightBackground": a(p["accent"], "14"),
        "editor.hoverHighlightBackground": a(p["accent"], "26"),
        "editor.foldBackground": a(p["accent"], "14"),
        "editorLink.activeForeground": p["link"],
        "editorWhitespace.foreground": a(p["fgDim"], "55"),
        "editorIndentGuide.background1": a(p["fgMuted"], "26"),
        "editorIndentGuide.activeBackground1": a(p["accent"], "88"),
        "editorRuler.foreground": a(p["fgMuted"], "26"),
        "editorCodeLens.foreground": p["fgDim"],
        "editorBracketMatch.background": a(p["accent"], "26"),
        "editorBracketMatch.border": a(p["accent"], "99"),
        "editorGhostText.foreground": a(p["fgMuted"], "99"),
        "editorInlayHint.background": a(p["bgDeep"], "AA"),
        "editorInlayHint.foreground": p["fgMuted"],
        "editorUnnecessaryCode.opacity": "#000000AA",
        "editorError.foreground": p["error"],
        "editorWarning.foreground": p["warning"],
        "editorInfo.foreground": p["info"],
        "editorHint.foreground": p["accent2"],
        "editorStickyScroll.background": p["bg"],
        "editorStickyScroll.shadow": p["shadow"],
        "editorStickyScrollHover.background": p["bgHover"],
    })
    for i, color in enumerate(p["brackets"], start=1):
        c[f"editorBracketHighlight.foreground{i}"] = color
    c["editorBracketHighlight.unexpectedBracket.foreground"] = p["error"]

    # --- gutter / overview ruler / minimap ------------------------------------
    c.update({
        "editorGutter.background": p["bg"],
        "editorGutter.modifiedBackground": p["modified"],
        "editorGutter.addedBackground": p["added"],
        "editorGutter.deletedBackground": p["deleted"],
        "editorOverviewRuler.border": "#00000000",
        "editorOverviewRuler.findMatchForeground": a(p["string"], "AA"),
        "editorOverviewRuler.errorForeground": p["error"],
        "editorOverviewRuler.warningForeground": p["warning"],
        "editorOverviewRuler.infoForeground": p["info"],
        "editorOverviewRuler.modifiedForeground": a(p["modified"], "AA"),
        "editorOverviewRuler.addedForeground": a(p["added"], "AA"),
        "editorOverviewRuler.deletedForeground": a(p["deleted"], "AA"),
        "minimap.background": p["bg"],
        "minimap.findMatchHighlight": a(p["string"], "AA"),
        "minimap.selectionHighlight": a(p["accent"], "88"),
        "minimapSlider.background": a(p["accent"], "1F"),
        "minimapSlider.hoverBackground": a(p["accent"], "33"),
        "minimapSlider.activeBackground": a(p["accent"], "4D"),
        "minimapGutter.addedBackground": p["added"],
        "minimapGutter.modifiedBackground": p["modified"],
        "minimapGutter.deletedBackground": p["deleted"],
    })

    # --- widgets flutuantes ---------------------------------------------------
    c.update({
        "editorWidget.background": p["bgWidget"],
        "editorWidget.foreground": p["fg"],
        "editorWidget.border": p["borderStrong"],
        "editorWidget.resizeBorder": p["accent"],
        "editorSuggestWidget.background": p["bgWidget"],
        "editorSuggestWidget.border": p["borderStrong"],
        "editorSuggestWidget.foreground": p["fg"],
        "editorSuggestWidget.selectedBackground": p["bgActive"],
        "editorSuggestWidget.selectedForeground": p["fg"],
        "editorSuggestWidget.highlightForeground": p["accent"] if dark else "#0F6FA8",
        "editorSuggestWidget.focusHighlightForeground": p["accent"] if dark else "#0F6FA8",
        "editorHoverWidget.background": p["bgWidget"],
        "editorHoverWidget.border": p["borderStrong"],
        "editorHoverWidget.foreground": p["fg"],
        "editorHoverWidget.statusBarBackground": p["bgDeep"],
        "debugToolBar.background": p["bgWidget"],
        "debugToolBar.border": p["borderStrong"],
    })

    # --- peek view ------------------------------------------------------------
    c.update({
        "peekView.border": p["accent"],
        "peekViewEditor.background": p["bgDeep"],
        "peekViewEditor.matchHighlightBackground": p["findMatch"],
        "peekViewEditorGutter.background": p["bgDeep"],
        "peekViewResult.background": p["bgAlt"],
        "peekViewResult.selectionBackground": p["bgActive"],
        "peekViewResult.selectionForeground": p["fg"],
        "peekViewResult.matchHighlightBackground": p["findMatch"],
        "peekViewResult.fileForeground": p["fg"],
        "peekViewResult.lineForeground": p["fgMuted"],
        "peekViewTitle.background": p["bgWidget"],
        "peekViewTitleLabel.foreground": p["fg"],
        "peekViewTitleDescription.foreground": p["fgMuted"],
    })

    # --- diff -----------------------------------------------------------------
    c.update({
        "diffEditor.insertedTextBackground": a(p["added"], "2E"),
        "diffEditor.removedTextBackground": a(p["deleted"], "2E"),
        "diffEditor.insertedLineBackground": a(p["added"], "17"),
        "diffEditor.removedLineBackground": a(p["deleted"], "17"),
        "diffEditor.diagonalFill": a(p["fgDim"], "33"),
        "diffEditor.border": p["border"],
    })

    # --- scrollbars -----------------------------------------------------------
    c.update({
        "scrollbar.shadow": "#00000000",
        "scrollbarSlider.background": a(p["accent"], "33"),
        "scrollbarSlider.hoverBackground": a(p["accent"], "55"),
        "scrollbarSlider.activeBackground": a(p["accent"], "77"),
    })

    # --- controles ------------------------------------------------------------
    c.update({
        "input.background": p["bgInput"],
        "input.foreground": p["fg"],
        "input.border": p["borderStrong"],
        "input.placeholderForeground": p["fgDim"],
        "inputOption.activeBackground": a(p["accent"], "33"),
        "inputOption.activeBorder": p["accent"],
        "inputOption.activeForeground": p["fg"],
        "inputValidation.errorBackground": p["bgWidget"],
        "inputValidation.errorBorder": p["error"],
        "inputValidation.warningBackground": p["bgWidget"],
        "inputValidation.warningBorder": p["warning"],
        "inputValidation.infoBackground": p["bgWidget"],
        "inputValidation.infoBorder": p["info"],
        "dropdown.background": p["bgInput"],
        "dropdown.listBackground": p["bgWidget"],
        "dropdown.foreground": p["fg"],
        "dropdown.border": p["borderStrong"],
        "checkbox.background": p["bgInput"],
        "checkbox.foreground": p["fg"],
        "checkbox.border": p["borderStrong"],
        "button.background": p["button"],
        "button.foreground": p["buttonFg"],
        "button.hoverBackground": p["buttonHover"],
        "button.border": "#FFFFFF33",
        "button.separator": "#FFFFFF55",
        "button.secondaryBackground": p["headerBg"],
        "button.secondaryForeground": "#FFFFFF",
        "button.secondaryHoverBackground": "#379A4B",
        "badge.background": p["accent"] if dark else p["button"],
        "badge.foreground": "#04263A" if dark else "#FFFFFF",
        "progressBar.background": p["accent2"],
        "keybindingLabel.background": a(p["bgDeep"], "AA"),
        "keybindingLabel.foreground": p["fg"],
        "keybindingLabel.border": p["border"],
        "keybindingLabel.bottomBorder": p["borderStrong"],
    })

    # --- painel e terminal ----------------------------------------------------
    c.update({
        "panel.background": p["bgPanel"],
        "panel.border": p["borderStrong"],
        "panel.dropBorder": p["accent"],
        "panelTitle.activeBorder": p["accent"],
        "panelTitle.activeForeground": p["fg"],
        "panelTitle.inactiveForeground": p["fgMuted"],
        "panelSectionHeader.background": p["headerBg"],
        "panelSectionHeader.foreground": p["headerFg"],
        "panelInput.border": p["borderStrong"],
        "terminal.background": p["bgPanel"],
        "terminal.foreground": p["fg"],
        "terminal.selectionBackground": p["selection"],
        "terminal.border": p["border"],
        "terminalCursor.foreground": p["accent"] if dark else "#0F6FA8",
    })
    for name, color in p["ansi"].items():
        c[f"terminal.ansi{name}"] = color

    # --- barra de status ------------------------------------------------------
    c.update({
        "statusBar.background": p["statusBg"],
        "statusBar.foreground": p["statusFg"],
        "statusBar.border": "#FFFFFF33",
        "statusBar.noFolderBackground": p["statusAlt"],
        "statusBar.noFolderForeground": "#FFFFFF",
        "statusBar.debuggingBackground": p["statusDebug"],
        "statusBar.debuggingForeground": "#FFFFFF",
        "statusBarItem.hoverBackground": "#FFFFFF26",
        "statusBarItem.activeBackground": "#FFFFFF40",
        "statusBarItem.remoteBackground": p["statusAlt"],
        "statusBarItem.remoteForeground": "#FFFFFF",
        "statusBarItem.prominentBackground": "#FFFFFF26",
        "statusBarItem.errorBackground": "#C42B3C",
        "statusBarItem.errorForeground": "#FFFFFF",
        "statusBarItem.warningBackground": "#B86E00",
        "statusBarItem.warningForeground": "#FFFFFF",
    })

    # --- notificações, quick input, menus -------------------------------------
    c.update({
        "notifications.background": p["bgWidget"],
        "notifications.foreground": p["fg"],
        "notifications.border": p["borderStrong"],
        "notificationCenterHeader.background": p["bgDeep"],
        "notificationCenterHeader.foreground": p["fg"],
        "notificationToast.border": p["borderStrong"],
        "notificationsErrorIcon.foreground": p["error"],
        "notificationsWarningIcon.foreground": p["warning"],
        "notificationsInfoIcon.foreground": p["info"],
        "quickInput.background": p["bgWidget"],
        "quickInput.foreground": p["fg"],
        "quickInputTitle.background": p["bgDeep"],
        "quickInputList.focusBackground": p["bgActive"],
        "quickInputList.focusForeground": p["fg"],
        "quickInputList.focusIconForeground": p["fg"],
        "pickerGroup.foreground": p["accent"] if dark else "#0F6FA8",
        "pickerGroup.border": p["border"],
        "menu.background": p["bgWidget"],
        "menu.foreground": p["fg"],
        "menu.selectionBackground": p["bgActive"],
        "menu.selectionForeground": p["fg"],
        "menu.separatorBackground": p["border"],
        "menu.border": p["borderStrong"],
    })

    # --- decorações de git ----------------------------------------------------
    c.update({
        "gitDecoration.addedResourceForeground": p["added"],
        "gitDecoration.modifiedResourceForeground": p["modified"],
        "gitDecoration.deletedResourceForeground": p["deleted"],
        "gitDecoration.renamedResourceForeground": p["type"],
        "gitDecoration.untrackedResourceForeground": p["untracked"],
        "gitDecoration.ignoredResourceForeground": p["ignored"],
        "gitDecoration.conflictingResourceForeground": p["conflict"],
        "gitDecoration.submoduleResourceForeground": p["constant"],
    })

    # --- telas diversas -------------------------------------------------------
    c.update({
        "welcomePage.tileBackground": p["bgWidget"],
        "welcomePage.tileHoverBackground": a(p["accent"], "26"),
        "welcomePage.tileBorder": p["borderStrong"],
        "walkThrough.embeddedEditorBackground": p["bgDeep"],
        "settings.headerForeground": p["fg"],
        "settings.modifiedItemIndicator": p["accent"],
        "settings.focusedRowBackground": p["bgHover"],
        "settings.rowHoverBackground": p["bgHover"],
        "settings.focusedRowBorder": a(p["accent"], "66"),
        "chat.requestBackground": a(p["bgDeep"], "88"),
        "chat.requestBorder": p["border"],
        "chat.slashCommandBackground": a(p["accent"], "33"),
        "chat.slashCommandForeground": p["fg"],
        "editorMarkerNavigation.background": p["bgWidget"],
        "editorMarkerNavigationError.background": p["error"],
        "editorMarkerNavigationWarning.background": p["warning"],
        "editorMarkerNavigationInfo.background": p["info"],
    })

    return c
