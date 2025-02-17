# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['overlay.py'],
    pathex=[],
    binaries=[('C:\\Program Files\\Tesseract-OCR\\tesseract.exe', '.')],
    datas=[('config', 'config'), ('data', 'data'), ('assets', 'assets'), ('C:\\Program Files\\Tesseract-OCR\\tessdata', 'tessdata')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='overlay',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='overlay',
)
