const { ipcMain } = require('electron');
const screenshot = require('screenshot-desktop');
const axios = require('axios');
const FormData = require('form-data');

const ipcApi = (mainWindow) => {
    ipcMain.handle('print_helloword', async (event) => {
        return 'hello world';
    })


    // 鼠标穿透控制
    ipcMain.on('setIgnoreMouseEvents', async (event, flag) => {
        mainWindow.setIgnoreMouseEvents(flag, { forward: true });
    })

    // 开启屏幕检测
    ipcMain.on("startDetection", async (event) => {
        try {
            const imgBuffer = await screenshot({ format: 'png', quality: 100 });
            const form = new FormData();
            form.append('file', imgBuffer, 'screenshot.png');
            const { data: res } = await axios.post('http://38.46.31.194:2005/predict', form)
            mainWindow.webContents.send('detectionResult', res);
        } catch (err) {
            console.error('Error capturing screen:', err);
        }
    })

}

module.exports = ipcApi;