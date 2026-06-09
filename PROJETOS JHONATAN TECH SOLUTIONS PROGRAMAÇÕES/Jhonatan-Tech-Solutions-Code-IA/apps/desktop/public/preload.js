const { contextBridge, ipcMain } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  getVersion: () => ipcMain.invoke('get-app-version'),
  getAppPath: () => ipcMain.invoke('get-app-path')
});
