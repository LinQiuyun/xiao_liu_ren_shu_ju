# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['LightweightNotepad.py'],
    pathex=['D:\\LightweightNotepad'],
    binaries=[(r'D:\LightweightNotepad\venv\Lib\site-packages\torch_directml\DirectML.dll', 'torch_directml')],
    datas=[('D:\\LightweightNotepad\\LightweightNotepad\\icon\\main_icon.ico', 'icon')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LightweightNotepad',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\LightweightNotepad\\LightweightNotepad\\icon\\main_icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LightweightNotepad',
)
