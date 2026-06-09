const { app, BrowserWindow, Menu, ipcMain } = require('electron');
const isDev = require('electron-is-dev');
const path = require('path');

let mainWindow;

const createWindow = () => {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    },
    icon: path.join(__dirname, '../public/app-icon.png')
  });

  const startURL = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startURL);

  if (isDev) {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
};

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC Handlers
ipcMain.handle('get-app-version', () => {
  return app.getVersion();
});

ipcMain.handle('open-external', (event, url) => {
  require('electron').shell.openExternal(url);
});

// Menu
const menu = [
  {
    label: 'Arquivo',
    submenu: [
      { label: 'Sair', accelerator: 'CmdOrCtrl+Q', click: () => app.quit() }
    ]
  },
  {
    label: 'Edicao',
    submenu: [
      { label: 'Desfazer', accelerator: 'CmdOrCtrl+Z', role: 'undo' },
      { label: 'Refazer', accelerator: 'CmdOrCtrl+Y', role: 'redo' },
      { type: 'separator' },
      { label: 'Cortar', accelerator: 'CmdOrCtrl+X', role: 'cut' },
      { label: 'Copiar', accelerator: 'CmdOrCtrl+C', role: 'copy' },
      { label: 'Colar', accelerator: 'CmdOrCtrl+V', role: 'paste' }
    ]
  },
  {
    label: 'Ajuda',
    submenu: [
      {
        label: 'Sobre',
        click: () => {
          require('electron').dialog.showMessageBox(mainWindow, {
            type: 'info',
            title: 'Sobre JHONATAN CODE AI',
            message: 'JHONATAN TECH SOLUTIONS CODE AI',
            detail: 'Versao 1.0.0\n\nSistema IA para Engenharia de Software'
          });
        }
      }
    ]
  }
];

Menu.setApplicationMenu(Menu.buildFromTemplate(menu));
