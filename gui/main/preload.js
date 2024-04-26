const {ipcRenderer, contextBridge} = require('electron')

console.log('preload.js loaded');
// --------- Expose some API to the Renderer process ---------
contextBridge.exposeInMainWorld('ipcRenderer', {
  on(...args) {
    const [channel, listener] = args
    ipcRenderer.on(channel, (event, ...args) => listener(event, ...args))
  },
  off(...args) {
    const [channel, ...omit] = args
    ipcRenderer.off(channel, ...omit)
  },
  send(...args) {
    const [channel, ...omit] = args
    ipcRenderer.send(channel, ...omit)
  },
  invoke(...args) {
    const [channel, ...omit] = args
    return ipcRenderer.invoke(channel, ...omit)
  },
})
