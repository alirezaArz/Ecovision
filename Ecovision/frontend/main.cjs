const { app, BrowserWindow } = require("electron");
const path = require("path");

app.disableHardwareAcceleration();

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      preload: path.join(__dirname, "preload.js"),
      webSecurity: false,
    },
  });

  const startURL =
    process.env.NODE_ENV === "development"
      ? `http://127.0.0.1:${process.env.VITE_DEV_SERVER_PORT || 5173}`
      : `file://${path.join(app.getAppPath(), "dist", "index.html")}`;

  win.loadURL(startURL);

  if (process.env.NODE_ENV === "development") {
    win.webContents.openDevTools();
  }
}

app.whenReady().then(() => {
  createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
