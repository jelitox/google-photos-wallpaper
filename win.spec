# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\google-photos-wallpaper\\main.py'],
             pathex=['C:\\google-photos-wallpaper', 'C:\\google-photos-wallpaper'],
             binaries=[],
             datas=[
                ('env/lib/site-packages/eel/eel.js', 'eel'),
                ('web', 'web'),
                ('storage/options.json', 'storage'),
                ('src/client_secrets.json', 'src'),
                ('src/icon.png', 'src')
            ],
             hiddenimports=[],
             hookspath=['c:\\google-photos-wallpaper\\env\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='win')
