const { app, BrowserWindow } = require('electron')
const path = require('node:path')
const ipcApi = require('./utils/ipcApi.js')

// try {
// 	require('electron-reloader')(module);
// } catch {}


var win = null
const createWindow = () => {
    win = new BrowserWindow({
        // 全屏
        fullscreen: true,
        // 无边框
        frame: false,
        // 透明
        transparent: true,
        // 无菜单
        autoHideMenuBar: true,
        // 禁止最大化
        maximizable: false,
        // 禁止调整大小
        resizable: false,
        // 不在任务栏显示
        skipTaskbar: true,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
        },
    })
    win.setAlwaysOnTop(true, 'screen-saver')
    // preload.js
    win.loadFile('page/index.html')
    win.webContents.openDevTools()
    ipcApi(win)
}


app.whenReady().then(() => {
    createWindow()
})
